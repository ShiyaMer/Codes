class Solution:
    #Function to find the minimum element in the given BST.
    def minValue(self, root):
        if not root:
            return -1
        cur=root
        while(cur.left):
            cur=cur.left
        return cur.data     
