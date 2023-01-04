# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)



def factorial(n):
    factorial=1
    for i in range(2,n+1):
        factorial=i*factorial
    return factorial
          
result=factorial(5)
print(result)