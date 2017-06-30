# -*- coding: utf-8 -*-

from simplesqlite import SimpleSQLite
from footballparser.data.jppldata2017 import Jppldata

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
        
        
        
    def __del__( self ):
        if self.con is not None:
            self.con.close()
        
if __name__ == "__main__":
   
    sqlClient = SqliteCilent()
    colums = ['a','b','c']
    sqlClient.createTableWithList("test",colums)
    sqlClient.insertOneRow("test",colums)