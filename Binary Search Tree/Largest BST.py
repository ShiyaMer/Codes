Brute:
class Solution:
    # Return the size of the largest sub-tree which is also a BST
   
    def validate(self,root,low,high):
        if not root:
            return True
            
        if low>=root.data or root.data>=high:
            return False
        return self.validate(root.left,low,root.data) and self.validate(root.right,root.data,high)
    
        
    def size(self,root):
        if not root:
            return 0
        return 1+self.size(root.left)+self.size(root.right)        
        
    def largestBst(self, root):
        if self.validate(root,-float('inf'),float('inf')):
            return self.size(root)
        return max(self.largestBst(root.left),self.largestBst(root.right)) 

#Optimal
class setnodevalue:
    def __init__(self,maxsize,maxnode,minnode):
        self.maxi=maxnode
        self.mini=minnode
        self.size=maxsize
#When i am checking from top to bottom left the largest(left)<current<smmalest(smallest)
#Dry run

class Solution:
    # Return the size of the largest sub-tree which is also a BST
    def helper(self,root):
        
        if not root:
            return setnodevalue(0,-float('inf'),float('inf'))
        left=self.helper(root.left)
        right=self.helper(root.right)
        if left.maxi<root.data and root.data<right.mini:
            return setnodevalue(left.size+right.size+1,max(right.maxi,root.data),min(left.mini,root.data))
        else:
            return setnodevalue(max(left.size,right.size),float('inf'),-float('inf'))
        
    def largestBst(self, root):
        return self.helper(root).size
