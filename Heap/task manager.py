from heapq import heappush,heappop,heapify 

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic=Counter(tasks)
        heap=[-cnt for cnt in dic.values()]
        heapify(heap)
        time=0
        q=deque()
        while(heap or q):
            time+=1
            if heap:
                cnt=1+heappop(heap)#since values negative this is equivalent to subtracting
                if cnt:
                    q.append([cnt,time+n]) 
            if q and q[0][1]==time:
                heappush(heap,q.popleft()[0])
        return time           
        
