#2 Queue
class MyStack(object):

    def __init__(self):
        self.q1=[]
        self.len=0
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q1.append(x)
        self.len+=1
        count=self.len
        while(count>1):
            self.q1.append(self.q1.pop(0))  
            count-=1
    def pop(self):
        """
        :rtype: int
        """
        if not self.q1:
            return -1
        self.len-=1    
        return self.q1.pop(0)
        

    def top(self):
        """
        :rtype: int
        """
        if not self.q1:
            return -1
        return self.q1[0]    

        

    def empty(self):
        """
        :rtype: bool
        """
        return not self.q1
        
#Using single queue
class MyStack(object):

    def __init__(self):
        self.q1=[]
        self.len=0
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q1.append(x)
        self.len+=1
        count=self.len
        while(count>1):
            self.q1.append(self.q1.pop(0))  
            count-=1
    def pop(self):
        """
        :rtype: int
        """
        if not self.q1:
            return -1
        self.len-=1    
        return self.q1.pop(0)
        

    def top(self):
        """
        :rtype: int
        """
        if not self.q1:
            return -1
        return self.q1[0]    

        

    def empty(self):
        """
        :rtype: bool
        """
        return not self.q1
        


