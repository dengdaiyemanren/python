# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*- 
'''
Created on 2017/6/17
@author: yinlg
'''
try:
    from httplib import HTTPConnection
except ImportError:
    from http.client import HTTPConnection
import urllib
from footballparser.util import vars as vs
#from tushare.stock import cons as ct

class Client(object):
    httpClient = None
    def __init__(self):
        self.httpClient = HTTPConnection(vs.HTTP_URL)
        
        
    def __del__( self ):
        if self.httpClient is not None:
            self.httpClient.close()
            
            
    def encodepath(self, path):
        start = 0
        n = len(path)
        re = ''
        i = path.find('=', start)
        while i != -1 :
            re += path[start:i+1]
            start = i+1
            i = path.find('&', start)
            if(i>=0):
                for j in range(start, i):
                    if(path[j] > '~'):
                        if vs.PY3:
                            re += urllib.parse.quote(path[j])
                        else:
                            re += urllib.quote(path[j])
                    else:
                        re += path[j]  
                re += '&'
                start = i+1
            else:
                for j in range(start, n):
                    if(path[j] > '~'):
                        if vs.PY3:
                            re += urllib.parse.quote(path[j])
                        else:
                            re += urllib.quote(path[j])
                    else:
                        re += path[j]  
                start = n
            i = path.find('=', start)
        return re
          
        
    def getData(self, path):
        result = None
        path='/league/scoreresult!ajaxscoreResult.htm?' + path
        path=self.encodepath(path)
        try:
            self.httpClient.request('GET', path,
                                    headers = {})
            response = self.httpClient.getresponse()
            if response.status == vs.HTTP_OK:
                result = response.read()
            else:
                result = response.read()
            if(path.find('.csv?') != -1):
                result=result.decode('GBK').encode('utf-8')
            return response.status, result
        except Exception as e:
            raise e
        return -1, result
