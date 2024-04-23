Brute:
def findMaxFruits(arr: List[int], n: int) -> int:
   #tress->0-n-1
   #fruit->1-n
   #2 baskets
    fruits=0
    for i in range(n):
        d={}
        dis=0
        count=0
        for j in range(i,n):
            if arr[j] not in d:
                d[arr[j]]=1
                dis+=1
            count+=1
            if dis>2:
                break
            fruits=max(fruits,count)
 optimal
def findMaxFruits(arr: List[int], n: int) -> int:
   #tress->0-n-1
   #fruit->1-n
   #2 baskets
    fruits=0
    i=0
    j=0
    dis=0
    d={}
    while(j<n):
        if arr[j] not in d:
            d[arr[j]]=1
        else:
            d[arr[j]]+=1    
        if len(d)>2:
            d[arr[i]]-=1
            if d[arr[i]]==0:
                del d[arr[i]]
            i+=1   
        if len(d)<=2:
            fruits=max(fruits,j-i+1) 
        j+=1     
        
    return  fruits              

                


          
          
          
