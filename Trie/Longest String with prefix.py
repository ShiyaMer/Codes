
class TrieNode:
    def __init__(self):
        self.child={}
        self.end=False
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        cur=self.root
        for i in word:
            if i not in cur.child:
                cur.child[i]=TrieNode() 
            cur=cur.child[i]   
        cur.end=True      
    def checkforprefix(self,word):
        curr=self.root
        for i in word:
            curr=curr.child[i]
            if not curr.end:
                return False      
        return True                      


def completeString(n: int, a: List[str])-> str:
    
    # Write your Code here
    obj=Trie()
    for i in a:
        obj.insert(i)
    ans="" 
   
    for i in a:
        if obj.checkforprefix(i):
            if len(i)==len(ans):
                ans=min(i,ans)
            elif len(i)>len(ans):
                ans=i
    if ans=="":
        return None
    return ans               
                    
        

    pass
