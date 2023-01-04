# from pandas import array


# How to find the missing number in an integer array of 1 to 100?
myList=[x for x in range(1,101)]
myList.remove(73) #Missing Value


def findMissing(list,n):
    sum1=int(100*101/2)
    sum2=sum(list)
    print(sum1-sum2)
    
findMissing(myList,100)
