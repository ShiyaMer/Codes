from sys import *
from collections import *
from math import *

# Following is the Binary Tree node structure:
class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

def getTreeTraversal(root):
    stack=[[root,1]]
    pre=[]
    ino=[]
    post=[]
    if not root:
        return []
    while stack:
        if stack[-1][1]==1:
            pre.append(stack[-1][0].data)
            stack[-1][1]=2
            if stack[-1][0].left:
                stack.append([stack[-1][0].left,1])
        elif stack[-1][1]==2:
            ino.append(stack[-1][0].data)
            stack[-1][1]=3
            if stack[-1][0].right:
                stack.append([stack[-1][0].right,1])    
        else:
            post.append(stack[-1][0].data)
            stack.pop()           

    return [ino]+[pre]+[post]
