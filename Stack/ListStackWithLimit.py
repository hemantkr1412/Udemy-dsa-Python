class stack:
    def __init__(self,maxSize):
        self.maxsize=maxSize
        self.list=[]
        
    def __str__(self):
        values=self.list.reverse()
        values=[str(x) for x in self.list]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.list==[]:
            return True
        else:
            return False
    
    def isFull(self):
        if len(self.list)==self.maxsize:
            return True
        else:
            return False
    
    def push(self,value):
        if self.isFull():
            return "The Stack is full"
        else:
            self.list.append(value)
            return "The Element has been successfully inserted"
        
    def pop(self):
        if self.isEmpty():
            return "There is no any Element"
        else:
            return self.list.pop()
        
    
    def peek(self):
        if self.isEmpty():
            return "There is no any Element"
        else:
            return self.list[len(self.list)-1]
        
    def delete(self):
        self.list=None
    
    
customStack=stack(10)
# print(customStack.isFull())
# print(customStack.isEmpty())
customStack.push(0)
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
customStack.push(5)
customStack.push(6)
customStack.push(7)
customStack.push(8)
customStack.push(9)
customStack.push(10)
customStack.push(7)
customStack.push(7)
# print(customStack)
print(customStack.isFull())




        
        