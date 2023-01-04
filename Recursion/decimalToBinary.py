#Deciml to binary using recursion



def decimalToBinary(n):
    assert int(n)==n , "Number must be integer"
    if n == 0:
        return 0
    else:
        return n%2 + 10*decimalToBinary(n//2)

print(decimalToBinary(10))