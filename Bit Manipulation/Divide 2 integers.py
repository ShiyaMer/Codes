Brute:
from typing import List

def divideTwoInteger(dividend: int, divisor: int) -> int:
    
    sign1,sign2=1,1
    if dividend<0:
       sign1=-1
       dividend=abs( dividend)
    if divisor<0:
        sign2=-1
        divisor=abs(divisor)
    sign=sign1*sign2
    if dividend==0 or dividend<divisor:
        return 0

    ans=0
    sum1=0
    while(dividend>=sum1+divisor):
        ans+=1
        sum1+=divisor
    ans=ans*sign
    if ans<-2**31:
        return -2**31
    if ans>2**31 -1:
        return 2**31 -1
    return ans    

Optimal:
from typing import List

def divideTwoInteger(dividend: int, divisor: int) -> int:
    #i can express any number in 2 's power so i shall remove the (highest power of 2 *divisor) at each try
    #ex div=22 di=3 ans=7
    #7 can be wrriten by p=2**2+2**1+2**0    3*p is nearly ==22
    sign1,sign2=1,1
    if dividend<0:
       sign1=-1
       dividend=abs( dividend)
    if divisor<0:
        sign2=-1
        divisor=abs(divisor)
    sign=sign1*sign2
    if dividend==0 or dividend<divisor:
        return 0
  
    ans=0 
    while(dividend>=divisor):
        mul=1
        tmp=divisor
        while(dividend>=tmp<<1):#tmp* to the power 2
            mul=mul<<1 #increment mul to the power 2
            tmp=tmp<<1# also invrement divisor *power of 2
        ans+=mul
        dividend-=tmp  #subtract calculated part
           

    ans=ans*sign
    if ans<-2**31:
        return -2**31
    if ans>2**31 -1:
        return 2**31 -1
    return ans    
