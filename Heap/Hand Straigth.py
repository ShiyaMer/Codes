from heapq import heapify,heappush,heappop
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if  groupSize==1:
            return True
        if len(hand)%groupSize!=0:
            return False
        heap=[]    
        d={}
        for i in hand:
            if i not in d:
                d[i]=1
                heappush(heap,i)
            else:
                d[i]+=1
        q=[]
        no_grp= len(hand)//groupSize       
        
   
        for i in range(no_grp):
            ele=heappop(heap)
            d[ele]-=1
            if d[ele]:
                q.append(ele)
            else:
                del d[ele]    
            for j in range(groupSize-1):
                if not heap:
                    return False
                ele2=heappop(heap)
                d[ele2]-=1
                if d[ele2]:
                    q.append(ele2)
                else:
                    del d[ele2]
                if ele2-ele!=1:
                    return False
                ele=ele2
            while(q):
                heappush(heap,q.pop(0))    
        return True            



        
