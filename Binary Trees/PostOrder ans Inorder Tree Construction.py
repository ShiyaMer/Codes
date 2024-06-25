# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        d={}
        for i in range(len(inorder)):
            d[inorder[i]]=i
        def tree(d,post,ino,ps,pe,ins,ine):
            if ps>pe and ins>ine:
                return
            root=TreeNode(post[ps])
            in_index=d[post[ps]]
            right_ele=ine-in_index
            root.right=tree(d,post,ino,ps+1,ps+right_ele,in_index+1,ine)
            root.left=tree(d,post,ino,ps+right_ele+1,pe,ins,in_index-1)
            return root
        postorder=postorder[::-1]
        n=len(postorder)
        return tree(d,postorder,inorder,0,n-1,0,n-1)    
        
