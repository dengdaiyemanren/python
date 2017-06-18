# -*- coding: utf-8 -*-

"""
equities = {
	'300001.SZ',
     '300002.SZ',
}
listobj = ['a','b','c']
dictobj = {'a':'1','b':'2'}

symbolsset = tuple(equities)
symbolsdict = tuple(dictobj)
symbolslistobj = tuple(listobj)

print(equities)
print(symbolsset)
print(listobj)
print(dictobj)
print(symbolsdict)
print(symbolslistobj)
"""
"""
def fab(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        yield b 
        # print b 
        a, b = b, a + b 
        n = n + 1 
for n in fab(5):
     print n
"""     


    ##import sys
    ##sys.path.insert(0, '../datatest')
    #print __file__
    #sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

import os
from . import datatest
equities = {
	'300001.SZ',
     '300002.SZ',
}
symbols = tuple(equities)
        
def _cachpath(symbol, type_):
    return '-'.join((symbol.replace(os.path.sep, '_'), type_))
for symbol in symbols:
    strstr = _cachpath(symbol,'ohlcv')
    print strstr


#path = _cachpath(symbol, 'ohlcv')