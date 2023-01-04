count=1
days=int(input("How many day's Temperature? "))
tempList=[]
while count <= days:
    temp = float(input("Day "+ str(count)+"'s high temp: "))
    tempList.append(temp)
    count=count+1
    
print("Average = ",sum(tempList)/len(tempList))
newlist=[x for x in tempList if x >sum(tempList)/len(tempList)]
print(len(newlist),"day(s) above average")
    