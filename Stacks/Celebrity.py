#Brute:
#User function Template for python3

class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        ind=[]
        col=len(M[0])
        for i in range(len(M)):
            if sum(M[i][0:col])==0:
                ind.append(i)

        if len(ind)==0:
            return -1
        for i in range(len(M)):
            if i!=ind[0] and M[i][ind[0]]==0 :
                return -1
        return ind[0]           
          
Optimal:
#User function Template for python3

class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):

     
        stack=[i for i in range(n)]
        while(len(stack)>=2):
            ind1=stack.pop()
            ind2=stack.pop()
            if M[ind1][ind2]==1 and M[ind2][ind1]==0:
                stack.append(ind2)
            elif M[ind2][ind1]==1 and  M[ind1][ind2]==0:
                stack.append(ind1)
           
        if not stack:
            return -1
           
        ind=stack[-1]
        if sum(M[ind][:])!=0:
            return -1
        for i in range(len(M)):
            if i!=ind and M[i][ind]!=1 :
                return -1
        return ind           
 




