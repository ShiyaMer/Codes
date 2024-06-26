class Solution:
    def findCeil(self,root, inp):
        # code here
        cur=root
        var=-1
        while(cur):
            if cur.key==inp:
                return cur.key
            elif cur.key<inp:
                cur=cur.right
            else:
                var=cur.key
                cur=cur.left
        return var    
