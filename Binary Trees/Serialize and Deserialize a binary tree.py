# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "#,"
        v=root.val    
        st=str(v)+','
        q=[root]
        while(q):
            i=len(q)
            for _ in range(i):
                node=q.pop(0)
                if node.left:
                    q.append(node.left)
                    st+=str(node.left.val)+','
                else:
                    st+='#,'
                if node.right:
                    q.append(node.right)
                    st+=str(node.right.val)+','
                else:
                    st+='#,' 
        return st                           

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data=data.split(',') 
        print(data)
        val=data.pop(0)
        if val=='#':
            return 
        root=TreeNode(int(val))
        q=[root]    
        while(q):
            node=q.pop(0)
            lef=data.pop(0)
            if lef!='#':
                node.left=TreeNode(int(lef))
                q.append(node.left)
            rig=data.pop(0) 
            if rig!='#':
                node.right=TreeNode(int(rig))
                q.append(node.right)
        return root        


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
