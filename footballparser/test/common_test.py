# -*- coding: utf-8 -*-
# -*- coding:utf-8 -*- 
'''
Created on 2017/6/17
@author: yinlg

httpclient test
'''
from footballparser.util.common  import  Client
import json
import pandas as pd

if __name__ == "__main__":
   # print "test"
    client = Client()
    
    path = "leagueId=33&season=2017&round=1&matchType=0"
    rsp = client.getData(path)
   ## print rsp[1]
    text = json.loads(rsp[1])
    ##print text
    filterjson =  text['result']['matchList']
   ## print filterjson
    
    ##print len(filterjson) == 0
    ##json = json.dumps(filterjson)
    
    ##print json
    
    
    fund_df = pd.DataFrame(filterjson,columns=['id','leagueName','hostTeamId','hostTeamName','awayTeamId','awayTeamName','hostScore','awayScore','status','winOdds','drawOdds','loseOdds'])
    
    ##fund_df.set_index(['id'])
    
    dfn = pd.DataFrame(columns=['id','leagueName','hostTeamId','hostTeamName','awayTeamId','awayTeamName','hostScore','awayScore','status','winOdds','drawOdds','loseOdds'])
    
    ##dfn.set_index(['id'])
    
    dfn = dfn.append(fund_df)
    
  
    def sumHostAndGuest(row,col1,col2):
        return row[col1] + row[col2]
    dff = dfn.apply(sumHostAndGuest,axis=1,col1='hostScore',col2='awayScore')
    
    dfn['sumScore'] = dff
    print dfn
    print dff
    print type (dff)