import heapq
class Solution:
    def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        arr=[-i for i in arr]
        heapq.heapify(arr)
        while(len(arr)!=k):
            heapq.heappop(arr)
        return -1*arr[0]    
           
