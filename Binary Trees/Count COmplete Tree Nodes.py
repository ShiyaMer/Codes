class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def find(root,p):#this works as no nodes present condition will be far left
            
            if not root:
                return 0
            c=0 
            if p:
                while(root):
                    c+=1
                    root=root.left
                return c   
            else:
                while(root):
                    c+=1
                    root=root.right
                return c 
        if not root:
            return 0
        lh=find(root,1)
        rh=find(root,0)
        if lh==rh:
            return ((2**lh) -1)
        return 1+self.countNodes(root.left)+self.countNodes(root.right)    

                 
                

            
            
        Brute:
      class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        stack=[root]
        ans=[]
        #Root,left,right
        while(stack):
            n=stack.pop()
            ans.append(n.val)
            if n.left:
                stack.append(n.left)
            if n.right:
                stack.append(n.right)  
        return len(ans)          
            
            
        
