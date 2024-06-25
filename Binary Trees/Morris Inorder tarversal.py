class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Morris Traversal o(1) space # i make dummmy links
        inorder=[]
        curr=root
        while(curr):
            if not curr.left:
                inorder.append(curr.val)#I have reached my leftmost position
                curr=curr.right
            else:
                #i need to assign connection between rightmost element of left node to the current node
                prev=curr.left
                while(prev.right and prev.right!=curr):
                    prev=prev.right
                if not prev.right:
                    prev.right=curr
                    curr=curr.left
                else:
                    prev.right=None
                    inorder.append(curr.val)#since i am at root before going right
                    curr=curr.right   
        return inorder                     
