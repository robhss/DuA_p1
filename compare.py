def compareData(path: str):

    with open(fr"{path}",'r') as f:
        list = f.readlines()

    result = []
    for i in list:
        i = i[:-1]                            
        result.append([i[:-(len(i) - i.index(" "))], i[i.index(" ") + 1:]])
           
    return result
