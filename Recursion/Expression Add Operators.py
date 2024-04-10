class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        ans=[]
        def solve(i,curr_res,val,prev):#i track previous to undo operation before multiplication
        #Ex 1+2*3=7 not 9
    
            if i>=len(num):
                if val==target:
                    ans.append("".join(curr_res))   
                return 
            for k in range(i,len(num)):
                
                curr_str=num[i:k+1]
                curr_num=int(curr_str)
                if not curr_res:
                    solve(k+1,[curr_str],curr_num,curr_num)
                else:
                    solve(k+1,curr_res+["+"]+[curr_str],val+curr_num,curr_num)
                    solve(k+1,curr_res+["-"]+[curr_str],val-curr_num,-curr_num)
                    solve(k+1,curr_res+["*"]+[curr_str],val-prev+curr_num*prev,curr_num*prev)#Precendence,undo
                if num[i]=='0':#Trailing zeros as #105 i cannot start with 0
                # not put in starting as only 0 as 1 element allowed but 
                #combiantion where 0 occuring in starting not allowed ex:05
                   break
        solve(0,[],0,0)
        return ans
        
        
