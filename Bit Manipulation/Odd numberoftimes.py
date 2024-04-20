def missingNumber(n: int, arr: List[int]) -> int:
    # Write your code here
    ans=arr[0]
    for i in range(1,n):
        ans=ans^arr[i]
    return ans
