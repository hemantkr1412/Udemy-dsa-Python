from ast import While
from unittest import result


def numberPalindromeOrNot(n):
    temp=n
    rev=0
    while n!=0:
        digit=n%10
        rev=rev*10+digit
        n=n//10
    if temp==rev:
        return "True"
    else:
        return "False"
    

resulT=numberPalindromeOrNot(121)
print(resulT)

