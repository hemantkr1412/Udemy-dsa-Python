


class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
            
class Stack:
    def __init__(self):
        self.Linkedlist=LinkedList()
        
    def __str__(self):
        values = [str(x.value) for x in self.Linkedlist]
        return '\n'.join(values)
            
    def isEmpty(self):
        if self.Linkedlist.head is None:
            return True
        else:
            return False
    
    def push(self,value):
        node=Node(value)
        node.next=self.Linkedlist.head
        self.Linkedlist.head=node
        
    def pop(self):
        if self.isEmpty():
            return "There is not any element"
        else:
            nodeValue=self.Linkedlist.head.value
            self.Linkedlist.head= self.Linkedlist.head.next
            return nodeValue
        
    def peek(self):
        if self.isEmpty():
            return "There is not any element"
        else:
            return self.Linkedlist.head.value
        
    def delete(self):
        self.Linkedlist.head=None
        
customStack=Stack()
customStack.push(1)    
customStack.push(2)
customStack.push(3) 
print(customStack)  

        
            
        
        