# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    #assign start from root (preorder and level order) x co-ordinates  and y- co-rdinates
    #the also store in dict when popping
    #travesr through dict
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q=[[root,0,0]]
        d={}
        while(q):
            i=len(q)
            for _ in range(i):
                n=q.pop(0)
                node=n[0]
                x=n[1]
                y=n[2]
                if node.left:
                    q.append([node.left,x-1,y+1])
                if node.right:
                    q.append([node.right,x+1,y+1])
                if x not in d:
                    d[x]=[]
                d[x].append((y,node.val))

        ans=[]       
        for i in sorted(d.keys()):
            temp=[]
            for j in sorted(d[i]):#in case of tie y i need it sorted hece taken care of
                temp.append(j[1])
            ans.append(temp)
        return ans        


        return ans    

                


        
