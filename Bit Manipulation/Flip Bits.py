def flipBits(A : int, B : int) -> int:
    c=A^B
    count=0
    while(c):
        c=c&(c-1)
        count+=1
    return count  
