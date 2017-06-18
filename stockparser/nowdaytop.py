# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*- 
'''
Created on 2017/6/17
@author: yinlg
获取当天换手率最大的股票信息
todo:为了得到有参考价值的数据，可以尝试抹掉末尾数
'''
import tushare as ts

class NowDayTopStock(object):
    def __init__(self):
        self.df = ts.get_today_all()
        self.stockdf = ts.get_stock_basics()
         
        
    """
        获取当日换手率排行靠前或者靠后的股票
    """
    def getTopTurnOverrateStock(self,n,ascending=False):
        self.n = n
        self.ascending = ascending
        sortdf= self.df.sort(columns='turnoverratio',ascending=self.ascending).head(n)
        ##print sortdf[['code','name','turnoverratio']]
        return sortdf
        
    """
        获取涨跌前几位的股票当日交易情况
    """
    def getTopRiseAndDownStock(self,n,ascending=False):
        self.n = n
        self.ascending = ascending
        sortdf= self.df.sort(columns='changepercent',ascending=self.ascending).head(n)
        return sortdf
    """
     按照指定的列来获取排序数据，比如按照换手率和涨幅来获取，排序方向是一致的
    """
    def getTopFactors(self,columns,n,ascending=[]):
        self.n = n
        self.ascending = ascending
        self.columns = columns
        sortdf= self.df.sort(columns = self.columns,ascending=self.ascending).head(n)
        return sortdf
        
    """
    获取PE的TOP股票，过滤掉不准确的值，比如为0的
    """
    def getTopPe(self,n,ascending=False):
        self.n = n
        self.ascending = ascending
        sortdf = self.stockdf.loc[self.stockdf.loc[:,'pe']>0].sort(columns="pe",ascending=self.ascending).head(n)
        return sortdf
        
        
 
        
        
        
 
        
        
        