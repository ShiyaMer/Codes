1  - 1
2 -  3
3-   0
4-   4

5 -1
6  -7
7 -0
8 -8
from typing import *

def findXOR(L : int, R : int) -> int:

    def func(n):
        if n%4==1:
            return 1
        if n%4==2:
            return n+1
        if n%4==3:
            return 0
        if n%4==0:
            return n
    L=func(L-1) #to include once
    R=func(R)
    return L^R                   
