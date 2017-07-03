# -*- coding: utf-8 -*-


def encodeList(fromList):
    toList = []
    for i in fromList:
        if isinstance(i, (str, unicode)):
            toList.append(i.encode("utf-8"))
        else:
            toList.append(i)         
    return toList
    
def encodeTupleList(fromTuple):
    toList = []
    
    for i in fromTuple:
        toList.append(encodeList(i))

    return tuple(toList)