# -*- coding:utf-8 -*- 
'''
Created on 2017/4/14
@author: yinlg
'''
import unittest
import tushare.stock.trading as fd
import tushare.stock.fundamental as fl
class Test(unittest.TestCase):
    def set_data(self):
        self.code = '000786'
        self.start = '2017-04-12'
        self.end = '2015-04-07'
        self.year = 2014
        self.quarter = 4
    def test_get_hist_data(self):
        self.set_data()
        print(fd.get_hist_data(self.code, self.start))
    
    def test_get_data(self):
        self.set_data()
        #print(fd.get_tick_data(self.code,self.start))
    def test_get_code(self):
        #print(fl.get_stock_basics())
        pass
    
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    
    test = 5
    print test**0.5
   ## unittest.main()    