class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #Brute
        def findpath(roo,arr,num):
            if not roo:
                return False
            arr.append(roo)
            if roo.val ==num.val:
                return True
            if findpath(roo.left,arr,num) or findpath(roo.right,arr,num):
                return True
            arr.pop(-1)
            return False
        arr1=[]
        findpath(root,arr1,p)
        arr2=[]
        findpath(root,arr2,q) 
        i=0
        node=TreeNode()
        while(i<len(arr1) and i<len(arr2)):
            if arr1[i]!=arr2[i]:
                break
            node=arr1[i]    
            i+=1
        return node
        #optimal
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root==p or root==q:
            return root
        left=self.lowestCommonAncestor(root.left, p, q)  
        right=self.lowestCommonAncestor(root.right, p, q) 
        if not left:
            return right
        elif not right:
            return left
        else:
            return root    
                           
                        


        
