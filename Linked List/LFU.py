class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.cnt=1
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.size=0  
        self.head=Node(-1,-1)
        self.tail=Node(-1,-1)  
        self.head.next=self.tail
        self.tail.prev=self.head

    def insert(self,node):
        temp=self.head.next
        node.prev=self.head
        node.next=temp
        temp.prev=node
        self.head.next=node
        self.size+=1

    def delete(self,node):
        previ=node.prev
        previ.next=node.next
        node.next.prev=previ
        self.size-=1    

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache={}
        self.freqlist={} #list of frequency with value being dll
        self.capacity=capacity
        self.minfreq=1

    def updatelist(self,node):
        del self.cache[node.key]
        self.freqlist[node.cnt].delete(node)
        if node.cnt==self.minfreq and self.freqlist[node.cnt].size==0:
            self.minfreq+=1
        nexthighdll=dll()
        if node.cnt+1 in  self.freqlist:
            nexthighdll=self.freqlist[node.cnt+1]
        node.cnt+=1
        nexthighdll.insert(node)
        self.freqlist[node.cnt]=nexthighdll
        self.cache[node.key]=node        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            node=self.cache[key]
            value=node.value
            self.updatelist(node)
            return value
        return -1    
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            node=self.cache[key]
            node.value=value#update and increase value of counter
            self.updatelist(node)
        else:
            if len(self.cache)==self.capacity:
                dl=self.freqlist[self.minfreq] #delete from min freq list end
                del self.cache[dl.tail.prev.key]
                dl.delete(dl.tail.prev) 
            self.minfreq=1# add the node
            listfreq=dll()
            if self.minfreq in self.freqlist:
                listfreq=self.freqlist[self.minfreq]
            node=Node(key,value)
            listfreq.insert(node)
            self.cache[key]=node
            self.freqlist[self.minfreq]=listfreq         
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
