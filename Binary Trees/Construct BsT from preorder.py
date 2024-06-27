Brute:
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        inorder=sorted(preorder)
        d={}
        for i in range(len(preorder)):
            d[inorder[i]]=i
        def helper(pre,ino,d,ps,pe,ins,ine):
            if ps>pe or ins>ine:
                return
            root=TreeNode(pre[ps])    
            in_or=d[pre[ps]]
            left=in_or-ins
            root.left=helper(pre,ino,d,ps+1,ps+left,ins,in_or-1)
            root.right=helper(pre,ino,d,ps+left+1,pe,in_or+1,ine)
            return root 
        n=len(preorder)       
        return helper(preorder,inorder,d,0,n-1,0,n-1)

Optimal:
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        i=[0]
        def helper(i,up,pre):
            if i[0]==len(pre) or pre[i[0]]>up:
                return
            root=TreeNode(pre[i[0]])
            i[0]+=1
            root.left=helper(i,root.val,pre)
            root.right=helper(i,up,pre)
            return root
        return helper(i,float('inf'),preorder)

