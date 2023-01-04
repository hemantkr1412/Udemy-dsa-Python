# Using String Sliceing


# def palindromeOrNot(Stirng):
#     if Stirng==String[::-1]:
#         return "Yes"
#     else:
#         return "No"                                                                                     



# Recursion


# def palindromeOrNot(Stirng):
#     if len(Stirng)<=1:
#         return "Yes"
#     else:
#         if Stirng[0]==Stirng[-1]:
#             return palindromeOrNot(Stirng[1:-1])
#         else:
#             return "No"
            
              

# Using Iteration

# def palindromeOrNot(Stirng):
#     while True:
#         if len(Stirng)<=1:
#             return "Yes"
#         elif Stirng[0]==Stirng[-1]:
#             Stirng=Stirng[1:-1]
#         else:
#             return "No"
        
# Using For Loop   
def palindromeOrNot(Stirng):
    n=len(Stirng)
    for i in range(len(Stirng)):
        if Stirng[i]!=Stirng[n-i-1]:
            return "No"
    return "Yes"
String="1111"
result=palindromeOrNot(String)
print(result)        

