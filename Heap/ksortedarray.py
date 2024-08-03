import heapq
class Solution:
    def heapsort(self,arr,k,n):
        d={}
        for i in range(n):
            d[arr[i]]=i
            
        heapq.heapify(arr)

        for i in range(n):
            if abs(d[heapq.heappop(arr)]-i)>k:
                return False
        return True 
        
        
    def isKSortedArray(self, arr, n, k): 
        l=self.heapsort(arr,k,n)
        if not l:
            return "No"
        return "Yes"    
