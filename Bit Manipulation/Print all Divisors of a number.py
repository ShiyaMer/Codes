from typing import List

def printDivisors(n: int) -> List[int]:
    count=[1]
    a=n
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            count.append(i)
            if (a//i)!=i:
                count.append(a//i)
    count.append(n)
    count.sort()
    return count            
