#using set Method

# def secondHighest(lst):
    
#     lst=list(set(lst))
#     print(lst)
#     return lst[-2]



def secondHighestNumber(l):
    if l[0]>l[1]:
        first=l[0]
        second=l[1]
    else:
        first=l[1]
        second=l[0]
    for i in range(2,len(l)):
        if l[i]>first:
            second=first
            first=l[i]
        elif l[i]>second and first!=l[i]:
            second=l[i]
    return second
    
result=secondHighestNumber([1,8,3,4,5,6,6,7,9,9])
print(result)