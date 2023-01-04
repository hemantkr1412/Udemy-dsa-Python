#Calculate the power of expoumber
def calculateThePower(base,expo):
    # assert pass
    if expo==0:
        return 1
    return base*calculateThePower(base,expo-1)

print(calculateThePower(5,2))
    