# Using Recursion
# def fibo(n):
#     assert n>=0 and int(n)==n , "Enter only Positive Integer"
#     if n==0 or n==1:
#         return n
#     else:
#         return fibo(n-1)+fibo(n-2)
    
# USing While Loop
# def fibo(n):
#     assert n>=0 and int(n)==n, "Enter Only Positive Integer"
#     i=1
#     prevnum1=0
#     prevnum2=1
#     while i<n:
#         cuurent=prevnum1+prevnum2
#         prevnum1=prevnum2
#         prevnum2=cuurent
#         i+=1
        
#     return cuurent

#Using For Loop
def fibo(n):
    assert n>=0 and int(n)==n, "Enter Only Positive Integer"
    
    prevnum1=0
    prevnum2=1
    for i in range(2,n+1):
        current=prevnum1+prevnum2
        prevnum1=prevnum2
        prevnum2=current
        
    return current

result = fibo(8)
print(result)
        
    

