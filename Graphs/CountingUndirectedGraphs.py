from typing import *

def countingGraphs(N: int) -> int:
   ans=(N*(N-1))//2
   #ans formula for the number of edges maximum
   #we can assume edge might be there or not
   return 2**ans  
