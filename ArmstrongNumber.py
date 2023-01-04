def armstrongNumOtNot(n):
    temp=n
    order=len(str(n))
    total=0
    while n!=0:
        digit=n%10
        total+=digit**order
        n=n//10
    if temp==total:
        return "Yes"
    else:
        return "No"

result=armstrongNumOtNot(153)
print(result)
        