class Solution:
    def floor(self, root, x):
        floor=-1
        cur=root
        while(cur):
            if cur.data==x:
               return x
            elif cur.data>x:
                cur=cur.left
            else:
                floor=cur.data
                cur=cur.right
        return floor   
