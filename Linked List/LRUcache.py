#put function:#i keep track of both key and value in DLL as it is easy to track when delting from cache
#->if existing then delete node create node and add to front
#if capacity exceed delete from end and insert at the new elment
#if not insert at head
#get:
# -1 if not in cache
#return value when found
#also delete the node and insert it at head when it is get as it comes recently accseed

class Node:

    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
        self.prev=None
class LRUCache:

    def __init__(self, capacity: int):
        self.cache={}
        self.capacity=capacity
        self.node=Node(-1,-1)
        self.head=self.node
        self.tail=self.node
    def get(self, key: int) -> int:
        if key in self.cache:
            node=self.cache[key]
            value=node.value
            if self.head.next==node:
                return value
            del self.cache[node.key]
            self.delete(node)
            #insertathead
            temp=Node(key,value)
            self.cache[key]=temp
            self.insertathead(temp)
            return value
        else:
            return -1    
    def delete(self,node):#at end
        if self.tail==node:
            temp=node.prev
            temp.next=None
            node.prev=None
            self.tail=temp
        else:
            temp=node.prev
            node.prev.next=node.next
            node.next.prev=node.prev

    def insertathead(self,node):
        if self.head==self.tail:
            self.head.next=node
            node.prev=self.head
            self.tail=node
        else:
            temp=self.head.next
            self.head.next=node
            node.next=temp
            node.prev=self.head
            temp.prev=node

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            delnode=self.cache[key]
            del self.cache[key]
            self.delete(delnode)
            node=Node(key,value)
            self.cache[key]=node
            self.insertathead(node)
        elif len(self.cache)<(self.capacity):
                node=Node(key,value)
                self.cache[key]=node
                self.insertathead(node)#
        else:
            nodetodelete=self.tail
            del self.cache[nodetodelete.key]
            self.delete(nodetodelete)
            #insertion
            nodetoinsert=Node(key,value)
            self.cache[key]=nodetoinsert
            self.insertathead(nodetoinsert)

                       
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
