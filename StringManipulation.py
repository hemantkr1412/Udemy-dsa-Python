def StringManipulation(s):
    lst=s.split("_")
    newlst=[]
    for i in lst:
        newlst.append(i[0].lower() + i[1:].upper())
        
    return ".".join(newlst)

s="This_is_Morning"
result=StringManipulation(s)
print(result)