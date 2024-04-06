class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
class MyQueue:
    
    #Function to push an element into the queue.
    def __init__(self): 
        self.front=None
        self.rear=None
        
        
    def push(self, item):
        node=Node(item)
        if self.front==None:
            self.front=node
            self.rear=node
            return
        self.rear.next=node
        self.rear=node
             
    #Function to pop front element from the queue.
    def pop(self):
        if self.front==None:
            return -1
        it=self.front.data
        self.front=self.front.next
        return it
