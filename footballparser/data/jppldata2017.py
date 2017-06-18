# -*- coding: utf-8 -*-

'''
日职赛数据统计2017
'''
from footballparser.util.common  import  Client
import json
import pandas as pd

class Jppldata(object):
    
    def __init__(self,year):
        self.year = year
        self.PATH= "leagueId=33&season=2017&matchType=0"
    def getData(self):
        i =1 
        round1 = 1
    
        client = Client()
        dfn = pd.DataFrame(columns=['leagueName','hostTeamId','hostTeamName',\
                     'awayTeamId','awayTeamName','hostScore','awayScore',\
                     'status','winOdds','drawOdds','loseOdds'])
        ##print dfn
        
        while i>0:
            
            fullpath = self.PATH + "&round=" +str(round1)
            #print fullpath

            rsp = client.getData(fullpath)
            filterjson =  json.loads(rsp[1])['result']['matchList']
            
            if len(filterjson) == 0:
                break
            
            df = pd.DataFrame(filterjson,\
                     columns=['leagueName','hostTeamId','hostTeamName',\
                     'awayTeamId','awayTeamName','hostScore','awayScore',\
                     'status','winOdds','drawOdds','loseOdds'])
            #print df
            dfn = dfn.append(df, ignore_index=True)
  
            round1 = round1 +  1
        self.df = dfn   
        return dfn
    def sumballoneplaystrategy(self,buy):
        
        sum =0 
        self.finsheddf = self.df.loc[self.df.loc[:,'status'] == 'COMPLETE']
        dff = self.finsheddf.apply(sumHostAndGuest,axis=1,col1='hostScore',col2='awayScore')
        df['sumScore'] = dff

        for one in buy:
           
           ##df1 = df.loc[df.loc[:,'sumScore'] == '1']
           sum = sum + len(df.loc[df.loc[:,'sumScore'] == one])
           
        return len(self.finsheddf),sum   
           
        
    def sumHostAndGuest(row,col1,col2):
        return row[col1] + row[col2]  

       
    '''
      设定几种投注方式：只投一场比赛，投一注：0，1，2
      只投一场比赛：投二注：0,1;0,2,1,2
      只投一场比赛：投三注：0，1，2，1，2，3
      假设比分系数为0：8倍；1：4倍；2：3倍；3，3倍
    '''
    def earnreateBysumoneplaystrategy(self,way): 
        zeropls = 8
        onepls = 4
        twopls =3
        threepls = 3
        
        susum0 = self.sumballoneplaystrategy([0.0])
        susum1 = self.sumballoneplaystrategy([1.0])  
        susum2 = self.sumballoneplaystrategy([2.0]) 
        susum3 = self.sumballoneplaystrategy([2.0])
        
        if way =='one':
  
            resultsum0 = susum0[1]*2*zeropls-susum0[0]*2
            resultsum1 = susum1[1]*2*onepls-susum0[0]*2
            resultsum2 = susum2[1]*2*twopls-susum0[0]*2

            return susum0[0],susum0[0]*2,"0",resultsum0,"1",resultsum1,'2',resultsum2

        elif way == 'two':
             
             resultsum01 =susum0[1]*2*zeropls + susum1[1]*2*onepls -susum0[0]*4
             resultsum02 =susum0[1]*2*zeropls + susum2[1]*2*twopls -susum0[0]*4
             resultsum12 =susum1[1]*2*onepls + susum2[1]*2*twopls -susum0[0]*4
            
             return susum0[0],susum0[0]*4,"01",resultsum01,"02",resultsum02,'12',resultsum12

        elif way == 'three':
            
            resultsum012 =susum0[1]*2*zeropls + susum1[1]*2*onepls+ susum2[1]*2*twopls -susum0[0]*6
            resultsum123 =susum1[1]*2*onepls + susum2[1]*2*twopls+ susum3[1]*2*threepls -susum0[0]*6
            
            return susum0[0],susum0[0]*6,"012",resultsum012,"123",resultsum123
        else:
           pass
        

        
if __name__ == "__main__":
    data = Jppldata("2017")
    df = data.getData()
    #sum0 = data.sumballoneplaystrategy([0.0])
    ##sum1 = data.sumballoneplaystrategy([1.0])
    #sum2 = data.sumballoneplaystrategy([2.0])
    
    '''
      (131, 262, '0', -198, '1', 2, '2', -34)
      (131, 524, '01', -196, '02', -232, '12', -32)
      (131, 786, '012', -230, '123', -66)
    '''
    earn1 =  data.earnreateBysumoneplaystrategy('one')
    print earn1
    earn2 =  data.earnreateBysumoneplaystrategy('two')
    print earn2
    earn3 =  data.earnreateBysumoneplaystrategy('three')
    print earn3
    
    
    