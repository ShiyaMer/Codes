class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class Stack:
    # Write your code here
    def __init__(self):
        self.count=0
        self.tail=None
        self.head=None
        
    def getSize(self):
        return self.count

    def isEmpty(self):
        return self.tail==None


    def push(self, data):
        node=Node(data)
        if self.tail==None:
            self.head=node
            self.tail=node
            self.count+=1
            return
        self.tail.next=node
        self.tail=node
        self.count+=1
        return

    def pop(self):
        if self.tail==None:
            return
        n=self.head
        while(n.next.next):
            n=n.next
        self.tail=n    
        n.next=None
        return        

    def getTop(self):
        if self.tail==None:
            return -1
        else:
            return self.tail.data    
        
