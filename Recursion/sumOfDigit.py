# Find the sum of Digit
def sumOfDigit(n):
    assert n>=0 and int(n)==n , "Enter only Positive integer Number"
    if n==0:
        return 0
    else:
        return int(n%10)+sumOfDigit(int(n//10))

print(sumOfDigit(int(input())))