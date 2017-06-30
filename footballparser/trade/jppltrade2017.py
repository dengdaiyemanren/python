# -*- coding: utf-8 -*-

from footballparser.util.sqliteclient import SqliteCilent
from footballparser.data.jppldata2017 import Jppldata

'''
1、历史数据记录
2、通过把每次的选择的数据记录到数据库中，计算总收益
3、通过历史数据辅助选择，逐步调整算法
4、最终可以考虑深度学习
'''
class Jppltrade(object):
    def __init__(self):
        self.sqlclient = SqliteCilent()
        
        self.jppldata = Jppldata("2017")
        self.__TableName__ ="jppldata2017"
        self.__TradeTableName__ = "jppldata2017_trade"
        self.__TradeTableColumnsName__ = ['leagueName','hostTeamId','hostTeamName',\
                     'awayTeamId','awayTeamName','hostScore','awayScore',\
                     'status','winOdds','drawOdds','loseOdds',\
                     'wishScores','wishScoresRate','wishHostScore','wishAwayScore','wishScoreRate']
        self.sqlclient.createTableWithList(self.__TradeTableName__,self.__TradeTableColumnsName__)
        
    def histToDb(self):
        self.sqlclient.dropTable("jppldata2017")
        self.sqlclient.createTableWithDf(self.jppldata.getData(),self.__TableName__)
    def pickyourfuck(self,row):
        
        self.sqlclient.insertOneRow(self.__TradeTableName__,row)
    
    def __del__(self):
        self.sqlclient.__del__()
    
        

if __name__ == "__main__":  
     jppltrade =  Jppltrade()
     row = ['1','2',7]   
     #jppltrade.pickyourfuck(row)
     ##jppltrade.histToDb()
     ##jppltrade.createTradeTable()
    