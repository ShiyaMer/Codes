from typing import List

class Solution:
    def __init__(self):
        self.trie = {}
    
    def insert(self, num):
        root = self.trie
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit not in root:
                root[bit] = {}
            root = root[bit]
    
    def search(self, num):
        root = self.trie
        if not root:
            return -1
        xor = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            nbit = 1 - bit
            if nbit in root:
                xor |= (1 << i)
                root = root[nbit]
            else:
                root = root[bit]
        return xor
    
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = [-1] * len(queries)  # Initialize with -1 as default answer
        d = {}
        queries=sorted(enumerate(queries),key=lambda x:x[1][1]) 
        nums.sort()
        idx = 0
        n = len(nums)
        for i,q in queries:
            x, m = q[0], q[1]
            while idx < n and nums[idx] <= m:
                self.insert(nums[idx])
                idx += 1
            g=self.search(x) 
            ans[i] =g
        
        return ans
