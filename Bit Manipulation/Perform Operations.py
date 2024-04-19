#Description:
#1. Get the bit value at the "i"th position of "num".

#2. Set the bit at the "i"th position of "num".

#3. Clear the bit at the "i"th position of "num".
Brute:
from typing import *

def bitManipulation(num : int, i : int) -> List[int]:
    def func(st,i):
        j=0
        su=0
        for i in st:
            su+=i*(2**j)
            j+=1
        return su    

    ans=[]
    st=[0]*32
    j=0
    while(num!=1 and num!=0):
        #print(num%2)
        st[j]=num%2
        num=num//2
        j+=1
    if num!=0:
        st[j]=1
    #print(st)
    ans.append(int(st[i-1]))
    st[i-1]=1
    ans.append(func(st,i))
    st[i-1]=0
    ans.append(func(st,i))
    return ans   
  Optimal:
def bitManipulation(num : int, i : int) -> List[int]:
     
    ans=[]

    ans.append(int(num&(1<<(i-1))!=0))

    ans.append(num|(1<<(i-1)))

    ans.append(num&(~(1<<(i-1))))
    return ans   

