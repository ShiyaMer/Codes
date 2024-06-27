class Solution:
    # returns the inorder successor of the Node x in BST (rooted at 'root')
    def inorderSuccessor(self, root, x):
        cur=None
        while(root):
            if root.data<=x.data:
                root=root.right
            else:
                cur=root
                root=root.left
        return cur      
