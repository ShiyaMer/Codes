class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        #inorder travesal
        #sort #better approach is to compare the nodes while traversal
        #traverse the tree to find violation
        if not root:
            return
        voil1=None
        voil2=None
        def inorder(root,prev,voil1found):
            nonlocal voil1
            nonlocal voil2
            if not root:
                return None
            inorder(root.left,prev,voil1found)
            if prev[0] and prev[0].val>root.val:
                if not voil1found[0]:
                    voil1=prev[0]
                    voil2=root  
                    voil1found[0]=1
                else:
                    voil2=root
            else:
                prev[0]=root        
            inorder(root.right,prev,voil1found)  
        voil1found=[0]    
        inorder(root,[None],voil1found) 
        print(voil1)
        print(voil2)
        voil1.val,voil2.val=voil2.val,voil1.val   



        
