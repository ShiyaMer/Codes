class Solution:
    def maxScore(self, arr: List[int], k: int) -> int:
        maxi=-float("inf")
        #i can take first k elements
        #or i take lat k elments
        #or i can decrease from left and pick rightmost elemnts
        i=k-1
        n=len(arr)
        j=n-1
        left=sum(arr[:k])
        right=0
        while(j!=n-k-1):
            maxi=max(left+right,maxi)
            left-=arr[i]
            right+=arr[j]
            j-=1
            i-=1
        maxi=max(left+right,maxi)   
        return maxi   
