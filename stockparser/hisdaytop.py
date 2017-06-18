# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*- 
'''
Created on 2017/6/17
@author: yinlg
获取历史换手率最大的股票信息
todo:为了得到有参考价值的数据，可以尝试抹掉末尾数
'''

import tushare as ts
import pandas as pd

class HisDayTopStock(object):
    def __init__(self):
        self.stockbasicdf = ts.get_stock_basics()
        self.stocks = self.stockbasicdf.index.values.tolist()
        
    """
        获取历史某日换手率排行靠前或者靠后的股票,获取效率太低
    """
    def getTopTurnOverrateStock(self,n,startdate,enddate,ascending=False):
        self.n = n
        self.ascending = ascending
        ## df = ts.get_hists(self.stocks,start=startdate,end=startdate)
        df = pd.DataFrame()
        for symbol in self.stocks:
           i=0
           data = ts.get_hist_data(symbol, start=startdate, end=enddate)
           data['code'] = symbol
           i = i +1
           print i

           df = df.append(data, ignore_index=True) 
       
        sortdf= df.sort(columns='turnover',ascending=self.ascending).head(n)
        ##print sortdf[['code','name','turnoverratio']]
        return sortdf 
        
    """
        获取历史某日换手率排行靠前或者靠后的股票,获取效率太低,转为获取一部分数据
    """
    def getTopTurnOverrateStock2(self,stocks,n,startdate,enddate,ascending=False):    
        self.n = n
        self.ascending = ascending
        df = pd.DataFrame()
        for symbol in stocks:
            data = ts.get_hist_data(symbol, start=startdate, end=enddate)
            data['code'] = symbol
           
            df = df.append(data, ignore_index=True) 
        sortdf= df.sort(columns='turnover',ascending=self.ascending).head(n)     
        return  sortdf  
        
    """
        获取历史某日换手率排行靠前或者靠后的股票,获取效率太低
    """
    def getTopRiseAndDownStock(self,n,startdate,enddate,ascending=False):
        self.n = n
        self.ascending = ascending
        ## df = ts.get_hists(self.stocks,start=startdate,end=startdate)
        df = pd.DataFrame()
        for symbol in self.stocks:
           data = ts.get_hist_data(symbol, start=startdate, end=enddate)
           data['code'] = symbol

           df = df.append(data, ignore_index=True) 
       
        sortdf= df.sort(columns='p_change',ascending=self.ascending).head(n)
        ##print sortdf[['code','name','turnoverratio']]
        return sortdf         
        
    """
        获取历史某日换手率排行靠前或者靠后的股票,获取一部分数据
    """
    def getTopRiseAndDownStock2(self,stocks,n,startdate,enddate,ascending=False):
        self.n = n
        self.ascending = ascending
        ## df = ts.get_hists(self.stocks,start=startdate,end=startdate)
        df = pd.DataFrame()
        for symbol in stocks:
           data = ts.get_hist_data(symbol, start=startdate, end=enddate)
           data['code'] = symbol

           df = df.append(data, ignore_index=True) 
       
        sortdf= df.sort(columns='p_change',ascending=self.ascending).head(n)
        ##print sortdf[['code','name','turnoverratio']]
        return sortdf        
            
            
         