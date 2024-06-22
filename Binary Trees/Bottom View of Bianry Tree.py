class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
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
                if x not in d:
                    d[x]=node.data
                if node.left:
                    q.append([node.left,x-1,y+1])
                if node.right:
                    q.append([node.right,x+1,y+1])
        ans=[]
        for i in sorted(d.keys()):
            ans.append(d[i])
        return ans 
