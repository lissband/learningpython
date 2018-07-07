def copyDict(item):
    coppiedDict = {}
    for k,v in item.items():
        coppiedDict[k] = v
    return coppiedDict

print(copyDict({'a':123,'ban':'123'}))