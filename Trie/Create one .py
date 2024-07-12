class TrieNode:

    def __init__(self):
        self.child={}
        self.end=False
        
class Trie:

    def __init__(self):
        self.root=TrieNode()
        
    def insert(self, word: str) -> None:
        cur=self.root
        for i in word:
            if i not in cur.child:
                cur.child[i]=TrieNode()
            cur=cur.child[i]    
        cur.end=True    

    def search(self, word: str) -> bool:
        cur=self.root
        for i in word:
            if i not in cur.child:
                return False
            cur=cur.child[i]
        if cur.end==True:
            return True
        return False            
        

    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for i in prefix:
            if i not in cur.child:
                return False
            cur=cur.child[i]
       
        return True
                
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
