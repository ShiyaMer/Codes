class Solution:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        #find leaves
        leaves=set()
        TreeDict={}
        for tree in trees:
            TreeDict[tree.val]=tree
            if tree.left:
                leaves.add(tree.left.val)
            if tree.right:
                leaves.add(tree.right.val)
        #The root of my main tree cannot be same as a leafnode
        root=None
        for tree in trees:
            if tree.val not in leaves:
                root=tree
                break
        if root==None:
            return None
        # decide my current leaves as i go on appending to that
        curleaves={}
        if root.left:
            curleaves[root.left.val]=(-float('inf'),root.val,root,0)#here zero symbolizes left or right useful when joining later on
        if root.right:
            curleaves[root.right.val]=(root.val,float('inf'),root,1)

        del TreeDict[root.val]#i have decided my root .It is no longer a candidate for merging
        #Begin my merging process and validation.I have been given that only 3 node will ne present per tree
        while(TreeDict):
            Treefound=False
            for leaf,(up,high,parent,left_right_indicator) in curleaves.items():
                if leaf in TreeDict:
                    newTree=TreeDict[leaf]
                    del curleaves[leaf]
                    if newTree.left:
                        if up<newTree.left.val<high and newTree.left.val not in curleaves:
                            curleaves[newTree.left.val]=(up,newTree.val,newTree,0)
                        else:
                            return None#either out of bounds or duplicates boith of which not a bst    
                    if newTree.right:
                        if up<newTree.right.val<high and newTree.right.val not in curleaves:
                            curleaves[newTree.right.val]=(newTree.val,high,newTree,1)
                        else:
                            return None#either out of bounds or duplicates boith of which not a bst           
                    if left_right_indicator==0:
                        parent.left=newTree
                    else:
                        parent.right=newTree    
                    Treefound=True    
                    del TreeDict[newTree.val]
                    break

            if not Treefound:#as for both leaves i have not  found merging companions
                return None  
        return root                            


