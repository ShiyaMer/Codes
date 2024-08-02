def left(i):
    return 2*i+1
def right(i):
    return 2*i+2
    
class Solution:
    def isMaxHeap(self,arr,n):
        for i in range(n//2,-1,-1):
            lef=left(i)
            rig=right(i)
            if (lef<n and arr[i]<arr[lef]) or (rig<n and arr[i]<arr[rig]):
                return False
        return True    
