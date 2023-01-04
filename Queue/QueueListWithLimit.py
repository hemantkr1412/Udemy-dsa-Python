

class Queue:
    def __init__(self,maxsize):
        self.list=maxsize*[None]
        self.maxsize=maxsize
        self.start=-1
        self.top=-1
        
    def __str__(self):
        values=[str(x) for x in self.list]
        return ' '.join(values)
    
    def isEmpty(self):
        if self.top==-1:
            return True
        else:
            return False
    
    def isFull(self):
        if self.top+1==self.start:
            return True
        elif self.start==0 and self.top+1==self.maxsize:
            return True
        else:
            return False
    
    def enqueue(self,value):
        if self.isFull():
            return "Queue is Full"
        else:
            if self.top+1==self.maxsize:
                self.top=0
            else:
                self.top+=1
                if self.start==-1:
                    self.start=0
            self.list[self.top]=value
            return "The element is inserted"
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            
        
        
customQueue=Queue(5)
print(customQueue.isEmpty())
print(customQueue.isFull())
customQueue.enqueue(1)
customQueue.enqueue(2)
print(customQueue)