class MyQueue(object):

    def __init__(self):
        self.stack1=[]
        self.stack2=[]
        self.len=0

    def push(self, x):
        while(self.stack1):
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        while(self.stack2):
            self.stack1.append(self.stack2.pop())
        self.len+=1
    def pop(self):
        """
        :rtype: int
        """
        if not self.stack1:
            return -1
        self.len-=1    
        return self.stack1.pop()    
        

    def peek(self):
        """
        :rtype: int
        """
        if not self.stack1:
            return -1
        return self.stack1[self.len-1]   
        
        

    def empty(self):
        """
        :rtype: bool
        """
        return not self.stack1
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
