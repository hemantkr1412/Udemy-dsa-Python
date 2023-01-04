from xml.dom.minidom import Element

from matplotlib.cbook import Stack


class stack:
    def __init__(self):
        self.list=[]
    
    def __str__(self):
        if self.list is None:
            return "List does not have any element"
        values=self.list.reverse()
        values=[str(x) for x in self.list]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.list==[]:
            return True
        else:
            return False
        
    
    def push(self,value):
        self.list.append(value)
        return "The element has been sucessfully inserted"

    def pop(self):
        if self.isEmpty():
            return "There are no any element"
        else:
            return self.list.pop()
        
    # return the top Element of stack
    def peek(self):
        if self.isEmpty():
            return "There is no any element"
        else:
            return self.list[len(self.list)-1]
        
    # delete Entire Stack
    def delete(self):
        self.list=None
        
        

customStack=stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
# print(customStack.pop())
# print(customStack.peek())
customStack.delete()
print(customStack)
        
        