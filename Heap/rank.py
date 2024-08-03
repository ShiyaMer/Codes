import heapq
class Solution:
    def replaceWithRank(self, N, arr):
        d={}
        for i in range(N):
            if arr[i] not in d:
                d[arr[i]]=[]
            d[arr[i]].append(i)   
        l=arr[:]
        heapq.heapify(l)
        
        rank=1
        while(l):
            ele=heapq.heappop(l)

            temp=d[ele]
            for ind in temp:
                arr[ind]=rank
            d[ele]=[]
            if temp:
                rank+=1
        return arr
