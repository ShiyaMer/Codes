class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack=[]
        self.root=root
        cur=self.root
        while(cur):
            self.stack.append(cur)
            cur=cur.left
    def next(self) -> int:
        if len(self.stack):
            node=self.stack.pop()
            if node.right:
                self.stack.append(node.right)
                cur=node.right
                while(cur.left):
                    self.stack.append(cur.left)
                    cur=cur.left
            return node.val        
        else:
            return -1    

    def hasNext(self) -> bool:
        return len(self.stack)!=0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
