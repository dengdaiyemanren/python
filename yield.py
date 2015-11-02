# -*- coding: utf8 -*-

def fab(max):
    n,a,b = 0,0,1
    while n < max:
        print b
        a,b = b,a+b
        n = n +1
#fab(5)

def fabx0(max):
    n,a,b = 0,0,1
    L = []
    while n < max:
        L.append(b)
        a,b = b , a+b
        n = n + 1
    return L

       
def fab01(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n = n +1
        
for xx in fab01(5):
    print xx   

f = fab01(5)
print f.next()

## 使用 isgeneratorfunction 判断 ##
from inspect import isgeneratorfunction

print isgeneratorfunction(fab01) 

 
import types 
print isinstance(fab01, types.GeneratorType) 
    
print isinstance(fab01(5), types.GeneratorType)     
    