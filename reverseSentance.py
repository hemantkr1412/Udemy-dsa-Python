# Sen="I am Hemant"
# def reverseSentance(sen):
#     senlst=sen.split()
#     senlst=senlst[::-1]
#     sen=" ".join(senlst)
#     return sen

 
# print(reverseSentance(Sen))


            
# Sen="I am Hemant"
# def reverseSentance(sen):
#     senlst=sen.split()
#     revLst=[]
#     for i in senlst:
#         revLst.insert(0,i)
#     return " ".join(revLst)

 
# print(reverseSentance(Sen)) 




Sen="I love my country"
def reverseSentance(sen):
    revSen=""
    word=""
    i=len(sen)-1
    while i!=-1:
        if sen[i]==" ":
            word=word[::-1]
            
            
            revSen=revSen+word+" "
            word=""
        else:
            word=word+sen[i]
        i-=1
    return revSen+word[::-1]
        
 
print(reverseSentance(Sen)) 