from itertools import count
from tracemalloc import start
from turtle import st
from unittest import result
import time

# def countAplbhabet(String):
#     String=String.upper()
#     lst=[]  
#     count_dict={}  
#     for i in String:
#         if i not in lst:
#             lst.append(i)
#             count=String.count(i)
#             count_dict[i]=count
            
#     return count_dict

# input_string=input("Enter Your String ")
# result=countAplbhabet(input_string)
# for i in result:
#     print(i," : ",result[i])



def countAlphabet(String):
    String=String.upper()
    dict_c={}
    for i in String:
        count_=0
        for j in String:
            if i==j:
                count_ +=1
        dict_c[i]=count_
        
    return dict_c      

start=time.time()  
print(countAlphabet("Elephant"))
print(time.time()-start)
