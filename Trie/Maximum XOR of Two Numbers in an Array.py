class Solution:
    def __init__(self):
        self.trie={}
    def insert(self,num):
        root=self.trie
        for i in range(31,-1,-1):
            #right shift divide by 2
            bit=(num>>i)&1
            if bit not in root:
                root[bit]={}
            root=root[bit]    

    def search(self,num):
        root=self.trie
        xor=0
        for i in range(31,-1,-1):
            bit=(num>>i)&1
            nbit=1-bit
            if nbit in root:
                xor=xor|1<<i  #2 to the power i
                root=root[nbit]
            else:
                root=root[bit]  
      
        return xor         

    def findMaximumXOR(self, nums: List[int]) -> int:
        for i in nums:
            self.insert(i)
        maxi=0    
        for i in nums:
            maxi=max(self.search(i),maxi)
        return maxi    

        
