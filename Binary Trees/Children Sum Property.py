Brute:
def changeTree(root): 
    def help(root):
        if not root:
            return 0
        left=help(root.left)
        right=help(root.right)    
        currsum=left+right
        currdiff=currsum-root.data
        if currdiff>0:
            root.data+=currdiff
        elif root.left:
            root.left.data-=currdiff
            help(root.left)
        elif root.right:
            root.right.data-=currdiff 
            help(root.right)
        return root.data
    help(root)

    return root              
Optimal:
def changeTree(root): 
    def help(root):
        if not root:
            return 
        cursum=0    
        if root.left:
            cursum+=root.left.data
        if root.right:
            cursum+=root.right.data
        if cursum-root.data>=0:
            root.data+=cursum
        else:
            if root.left:
                root.left.data=root.data
            if root.right:
                root.right.data=root.data               
        help(root.left)
        help(root.right)  
        tot=0  
        if root.left:
            tot+=root.left.data
        if root.right:
            tot+=root.right.data  
        if root.left or root.right:
            root.data=tot    
        return       
    help(root)
    return root
  

            
