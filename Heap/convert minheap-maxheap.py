def left(i):
    return (2*i)+1
def right(i):
    return (2*i)+2
    
def maxheapify(i,N,arr):
    largest=i
    lef=left(i)
    rig=right(i)
    if lef<N and arr[lef]>arr[largest]:
        largest=lef
    if rig<N and arr[rig]>arr[largest]:
        largest=rig
    if i!=largest:
        arr[i],arr[largest]=arr[largest],arr[i]
        maxheapify(largest,N,arr)
class Solution:
    def convertMinToMaxHeap(self, N, arr):
        for i in range(N//2,-1,-1):
            maxheapify(i,N,arr)
