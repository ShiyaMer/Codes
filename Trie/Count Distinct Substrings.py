
#set solution tkaes a space complexity of n**3
class TrieNode:
    def __init__(self):
        self.d={}
def countDistinctSubstrings(s):
    root=TrieNode()
    count=0
    for i in range(len(s)):
        cur=root
        for j in range(i,len(s)):
            if s[j] not in cur.d:
               cur.d[s[j]]=TrieNode()
               count+=1
            cur=cur.d[s[j]]   


    return count+1       
            
