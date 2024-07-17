#User function Template for python3


#Function to delete a node from BST.
#i can replace the elemnt right before the key in inorder or the elemnt after the key in inorder.
#i choose after one
#Obtained by getting smallest elemt towards right
#why cause the leftmostmost elemnt will be easier to delete
#incase of only one child i just hav eto return the other child
#i copy the value of the righmost child and move forward
#and delete that leafnode.

def minval(root):
    while root.left:
        root=root.left
    return root.data    
def deleteNode(root, X):
    if not root:
        return root
    if X<root.data:
        root.left=deleteNode(root.left, X)
    elif X>root.data:
        root.right=deleteNode(root.right, X)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            root.data=minval(root.right)
            root.right=deleteNode(root.right, root.data)
            
    return root        
        

