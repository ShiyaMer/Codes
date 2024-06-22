#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
#left boundary :go left til left else right no leaf
#post/in/pre-any one trabveral for leaf when leaf
#right:separate stack for right then right if right else left no leaf put reverse of this the rest
class Solution:
    def printBoundaryView(self, root):
        stack=[]
        if not root:
            return stack
        def isleaf(node):
            if not node.left and not node.right:
               return True
            return False
        def leftboundary(node,stack):
            while(node):
                if not isleaf(node):
                    stack.append(node.data)
                if node.left:
                    node=node.left
                elif node.right:
                    node=node.right
                else:
                    break
        def leafinorder(node,stack):
            if not node:
                return
            leafinorder(node.left,stack)
            if isleaf(node) and node!=root:#single node case as i have already appended root
                stack.append(node.data)
            leafinorder(node.right,stack)   
        def rightboundary(node):
            revstack=[]
            while(node):
                if not isleaf(node):
                    revstack.append(node.data)
                if node.right:
                    node=node.right
                elif node.left:
                    node=node.left
                else:
                    break
            return revstack[::-1]
        stack.append(root.data)
        if root.left:
            leftboundary(root.left,stack)
        leafinorder(root,stack)
        if root.right:
            rev=rightboundary(root.right)
            stack.extend(rev)
        return stack    
                
            
                    
                
                



