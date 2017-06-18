# -*- coding:utf-8 -*- 
'''
Created on 2017/6/17
@author: yinlg

'''
from stockparser.hisdaytop  import  HisDayTopStock
from stockparser.nowdaytop  import  NowDayTopStock
  

import tushare as ts   

if __name__ == "__main__":
    print "test"
    histopStock = HisDayTopStock()
    nowtopStock = NowDayTopStock()
    
    df = nowtopStock.getTopTurnOverrateStock(10,False)
    
    stocks = df.loc[:,'code']
  
    
    df = histopStock.getTopTurnOverrateStock2(stocks,10,startdate='2017-06-15',enddate=None,ascending=False)
   ## df = ts.get_hists(["600312"],start="2017-06-16",end="2017-06-16")
   
   
    df = nowtopStock.getTopRiseAndDownStock(10,False)
   
    stocks = df.loc[:,'code']
   
    df = histopStock.getTopRiseAndDownStock2(stocks,10,startdate='2017-06-15',enddate=None,ascending=False)
   
    print df
