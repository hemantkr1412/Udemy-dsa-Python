

class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        
class singlyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
    # insert Node in Linked List
    def insertSLL(self,value,location):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        elif location==0:
            newNode.next=self.head
            self.head=newNode
        elif location==-1:
            newNode.next=None
            self.tail.next=newNode
            self.tail=newNode
        else:
                tempNode=self.head
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1
                nextNode=tempNode.next
                tempNode.next=newNode
                newNode.next= nextNode
                if tempNode==self.tail:
                    self.tail=newNode
    # Traverse SinglyLinkedList
    def traverse(self):
        if self.head is None:
            print("SinglyLinkedList is Empty")
        node=self.head
        while node is not None:
            print(node.value)
            node=node.next
            
    # Linked List search
    def searchSLL(self,nodeValue):
        if self.head is None:
            return "The List Does not Exits"
        node=self.head
        while node is not None:
            if node.value==nodeValue:
                return str(node.value)+" Exits"
            node=node.next
        return "The Value does not exits"
    
    # delete node From LinkedList
    def deleteNode(self,location):
        if self.head is None:
            print("Node does not exits")
        else:
            if location==0:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    # tempNode=self.head
                    # self.head=tempNode.next
                    self.head=self.head.next
            elif location==-1:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    node=self.head
                    while node is not None:
                        if node.next==self.tail:
                            break
                        node=node.next
                    node.next=None
                    self.tail=node
            else:
                tempNode=self.head
                index=0
                while index < location-1:
                    tempNode=tempNode.next
                    index+=1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
    
    
    def delteEntireSSL(self):
        if self.head is None:
            print("SSL does not extis")
        else:
            self.head=None
            self.tail=None
            
                    

        
                    
sLinkedlist=singlyLinkedList()
sLinkedlist.insertSLL(1,1)
sLinkedlist.insertSLL(2,-1)
sLinkedlist.insertSLL(3,-1)
sLinkedlist.insertSLL(0,0)
sLinkedlist.insertSLL(4,-1)
sLinkedlist.insertSLL(5,-1)
print([node.value for node in sLinkedlist])
# sLinkedlist.traverse()
# print(sLinkedlist.searchSLL(2))
# sLinkedlist.deleteNode(3)
sLinkedlist.delteEntireSSL()
print([node.value for node in sLinkedlist])
                
            
        