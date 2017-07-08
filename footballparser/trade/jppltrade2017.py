# -*- coding: utf-8 -*-

from footballparser.util.simplesqliteclient import SimpleSqliteCilent
from footballparser.data.jppldata2017 import Jppldata
#from footballparser.util.__encode__ import encodeTupleList

'''
1、历史数据记录
2、通过把每次的选择的数据记录到数据库中，计算总收益
3、通过历史数据辅助选择，逐步调整算法
4、最终可以考虑深度学习
'''
class Jppltrade(object):
    def __init__(self):
        self.sqlclient = SimpleSqliteCilent()
        
        self.jppldata = Jppldata("2017")
        self.__TableName__ ="jppldata2017"
        self.__TradeTableName__ = "jppldata2017_trade"
        self.__TradeTableColumnsName__ = ['matchTimeStr','leagueName','hostTeamId','hostTeamName',\
                     'awayTeamId','awayTeamName','hostScore','awayScore',\
                     'status','winOdds','drawOdds','loseOdds',\
                     'wishScores','wishScoresRate','wishHostScore','wishAwayScore','wishScoreRate']
        self.sqlclient.createTableWithList(self.__TradeTableName__,self.__TradeTableColumnsName__)
   
    '''
       历史记录入库
    '''
    def histToDb(self):
        self.sqlclient.dropTable("jppldata2017")
        self.sqlclient.createTableWithDf(self.jppldata.getData(),self.__TableName__)
    ##def insertRows(self,rows_dictList):
     ##   self.sqlclient.insertMany(self.__TradeTableName__,rows_dictList)
    
    
    '''
        返回未完成的数据,list返回
    '''
    def getNoStartData(self):
        #cond ="2017-07-08 00:00"
        dictCond ={"status":"NO_START"}
        data = self.sqlclient.query("jppldata2017",dictCond,"=",extra="order by matchTimeStr")
        print (data)  
        return data
    def parseWithHistData(self,onerow_list):  
        pass
        
        
    def __del__(self):
        self.sqlclient.__del__()
    
        

if __name__ == "__main__":  
     jppltrade =  Jppltrade()
     row = {}  
     sqlclient = SimpleSqliteCilent()
      ## create hist table begin 
     #jppltrade.histToDb()
     ## create hist table end

     '''
         获取未开始的记录 begin
     '''
     data = jppltrade.getNoStartData()
     print data[0][0]
  
     
     '''
       插入一条数据
     '''
    # rows_dictList=[{'matchTimeStr':,'leagueName':,}]
     rows_dictList =[ {'matchTimeStr':data[0][0],'leagueName':data[0][1],'hostTeamId':data[0][2],'hostTeamName':data[0][3],\
                     'awayTeamId':data[0][4],'awayTeamName':data[0][5]}]
     
     sqlclient.insertMany("jppldata2017_trade",rows_dictList);
     sqlclient.__del__()
         
     
     
     ##query demo begin
     #dictCond ={"hostTeamId":230}
     #result = sqlclient.query("jppldata2017",dictCond)
     ## query demo end
     
   
     ### insert demo begin
     #insertDictList =  [{"leagueName":"111"},{"leagueName":"222"}]  
     #sqlclient1 = SqliteCilent()                   
     #sqlclient1.insertMany("jppldata2017_trade",insertDictList)                    
     ### insert demo end  
     
     
     
    ## 
     tuplelist =([111,222],[33,55])
     
     ##for tupleone in tuplelist:
       ##  print tupleone
     
     #jppltrade.pickyourfuck(row)
     ##jppltrade.histToDb()
     ##jppltrade.createTradeTable()
    