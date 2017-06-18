# -*- coding:utf-8 -*- 
'''
Created on 2017/6/17
@author: yinlg

'''

from stockparser.nowdaytop  import  NowDayTopStock
    
if __name__ == "__main__":
    print "test"
    topStock = NowDayTopStock()
    df = topStock.getTopTurnOverrateStock(10,False)
   ## print df[['code','name','changepercent','turnoverratio']]
    df = topStock.getTopRiseAndDownStock(5,False)
   # print df[['code','name','changepercent','turnoverratio']]
    df = topStock.getTopRiseAndDownStock(5,True)
    #print df[['code','name','changepercent','turnoverratio']]
    #df = topStock.getTopFactors(['turnoverratio','changepercent'],5,False)
    #df = topStock.getTopFactors(['changepercent','turnoverratio'],10,[True,False])
    
   # print df[['code','name','changepercent','turnoverratio']]
   
    df = topStock.getTopPe(5,False)
    print df