class TrieNode():
    def __init__(self):
        self.child={}
        self.end=False
        self.prefix=0
        self.count=0
class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self, word):
        cur=self.root
        for i in word:
            if i not in cur.child:
                cur.child[i]=TrieNode()
            cur=cur.child[i]#as in i have ap if i am doing for a there is a word that starts with a so the next word will be the indicator 
            cur.prefix+=1
        if not cur.end:
            cur.end=True
        cur.count+=1            

    def countWordsEqualTo(self, word):
        cur=self.root
        for i in word:
            if i not in cur.child:
                return 0
            cur=cur.child[i]
        return cur.count    

    def countWordsStartingWith(self, word):
        cur=self.root
        pre=0
        for i in word:
            if i not in cur.child:
                return 0    
            cur=cur.child[i]
        return cur.prefix
        

    def erase(self, word):
        cur=self.root
        for i in word:
            cur=cur.child[i]
            cur.prefix-=1
            
        cur.count-=1    
