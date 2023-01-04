#Normal Method
# def fizzBuzz(n):
#     if n%3==0 and n%5==0:
#         return "FizzBuzz"
#     elif n%5==0:
#         return "Buzz"
#     elif n%3==0:
#         return "Fizz"
#     else:
#         return n
    
#Using Dict

def fizzBuzz(n):
    d={3:"Fizz",
       5:"Buzz"}
    result=''
    for k,v in d.items():
        if n%k==0:
            result+=v
    if not result:
        result=n
    return result
            
    
    
result=fizzBuzz(45)
print(result)