Brute:
def helper(i, k, l, arr, n, target):
    if target == 0:
        l.append(k[:])
        return
    
    for j in range(i,n):
        if j>i and arr[j]==arr[j-1]:#to avoid duplicates the same elemnrts get avoided
           continue
        if arr[j]>target:
            break
        k.append(arr[j])
        helper(j + 1, k, l, arr, n, target - arr[j])
        k.pop()
def combinationSum(k: int, n: int) -> List[List[int]]:
    arr=[1,2,3,4,5,6,7,8,9]
    l = []
    helper(0, [], l, arr,9,n)
    f=[]
    for i in l:
        if len(i)==k:
            f.append(i)
    return f        
Better:
def helper(i, p, l, n,k,arr):
    if len(p)==k:
        if n== 0:
            l.append(p[:])
        return   
    for j in range(i,len(arr)):
        if j>i and arr[j]==arr[j-1]:
            continue
        if arr[j]>n:
            break
        p.append(arr[j])
        helper(j + 1, p, l,n-arr[j],k,arr)
        p.pop()       
def combinationSum(k: int, n: int) -> List[List[int]]:
    l = []
    temp=[]
    arr=[1,2,3,4,5,6,7,8,9]
    helper(0,temp, l,n,k,arr)
    return l        
