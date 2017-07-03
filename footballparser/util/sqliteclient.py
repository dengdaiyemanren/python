# -*- coding: utf-8 -*-

from simplesqlite import SimpleSQLite
from footballparser.data.jppldata2017 import Jppldata
from simplesqlite.sqlquery import SqlQuery
from footballparser.util.__error__ import NotSupportParamError

#import sqlite3
#conn = sqlite3.connect('test.db')
#print "Opened database successfully";

class SqliteCilent(object):
    def __init__(self):
        self.con = SimpleSQLite("pandas_df.sqlite")
    def createTableWithDf(self,dataframe,tableName):
        self.con.create_table_from_dataframe(dataframe,tableName)
        
    def dropTable(self,tableName):
        self.con.drop_table(tableName)
       
    def createTableWithList(self,tableName,columns):
        self.con.create_table(tableName,columns)
    def insertOneRow(self,tableName,columns):
        self.con.insert(tableName,columns)
        
    """
       返回的是tuple形式的结果
    """
    def query(self,tableName,whereDict):
        print len(whereDict.keys())
        print "---------------"
        if len(whereDict.keys()) != 1:
            raise NotSupportParamError()
        return self.con.select(select="*", table_name=tableName,\
                 where=SqlQuery.make_where(key=whereDict.keys()[0], value=whereDict[whereDict.keys()[0]])).fetchall()
    """
      根据where条件更新
    """
    def update(self,tableName,set_queryDict,whereDict):
          print len(whereDict.keys())
          print "---------------"
          if len(whereDict.keys()) != 1:
            raise NotSupportParamError()
            
          set_queryStr =""
          for setKey,setValue in set_queryDict.items():  
                 set_queryStr.join(setKey).join("=").join(setValue)
            
          return self.con.update(tableName,set_query ="", \
                                  where=SqlQuery.make_where(key=whereDict.keys()[0], \
                                     value=whereDict[whereDict.keys()[0]])).fetchall()
    
    """
     插入字典值形式的记录
    """
    def insertMany(self,tableName,inert_dictList):
         self.con.insert_many(tableName,inert_dictList)
         ##pass
        
    def __del__( self ):
        if self.con is not None:
            self.con.close()
        
if __name__ == "__main__":
   
    sqlClient = SqliteCilent()
   ## colums = ['a','b','c']
    ##sqlClient.createTableWithList("test",colums)
    ##sqlClient.insertOneRow("test",colums)
    dictCond ={"aa":10,"bb":20}
    print len(dictCond.keys())
   # for aa in dictCond.keys():
      #print aa
    sqlClient.__insertDemo__()
      

      
      
      