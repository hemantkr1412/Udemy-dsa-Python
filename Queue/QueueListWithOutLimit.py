class Queue:
    def __init__(self):
        self.list=[]
        
    def __str__(self):
        values=[str(x) for x in self.list]
        return " ".join(values)
        
    def isEmpty(self):
        if self.list==[]:
            return True
        else:
            return False
    
    def enqueue(self,value):
        self.list.append(value)
        return "The element is inserted at the end of Queue"
    
    def dequeue(self):
        if self.isEmpty():
            return "There is no any element"
        else:
            return self.list.pop(0)
        
    def peek(self):
        if self.isEmpty():
            return "Threr is no any Element"
        else:
            return self.list[0]
        
    
    def delete(self):
        self.list=None
        
customQueue=Queue()
print(customQueue.isEmpty())
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.enqueue(4)
customQueue.enqueue(5)
print(customQueue)
customQueue.dequeue()
print(customQueue)
print(customQueue.peek())
        