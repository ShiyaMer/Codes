class Solution:
    def minTime(self, root,target):
        if not root and  not target:
            return 0
        q0=[root]
        d={root:None}
        while(q0):
            i=len(q0)
            for _ in range(i):
                n=q0.pop(0)
                if n.data==target:
                    target=n
                if n.left:
                    d[n.left]=n
                    q0.append(n.left)
                if n.right:
                    d[n.right]=n
                    q0.append(n.right)
        visited=[]
        q=[target]
        dis=-1#as the first node is not counted
        while(q):
            i=len(q)
            l=[]
            for _ in range(i):
                n=q.pop(0)
                if n not in visited:
                    visited.append(n)
                if d[n] and (d[n] not in visited):
                    q.append(d[n])
                    visited.append(d[n])
                if n.left and n.left not in visited:
                    q.append(n.left)
                    visited.append(n.left)
                if n.right and n.right not in visited:
                    q.append(n.right)
                    visited.append(n.right)
            dis+=1
        return dis  
#Also possible approach:
you can also try it by slighly different approach. After making parent map, instead of taking another bfs to find the time, You can find the height  of tree  using dfs cosidering target node as root node and also taking the help of visited map. The code of this part is similar to find the height or bt with slight modification.

Code: 
int height(Node* root ,   unordered_map<Node*,Node*>&par ,  unordered_map<Node*, int>&vis)
{
    if(!root)
    return 0;
    
    vis[root]=1;
    
    int lh= INT_MIN;
     int rh= INT_MIN;
      int ph= INT_MIN;
    
    if(!vis[root->left])
     lh= height(root->left, par, vis);
      if(!vis[root->right])
        rh= height(root->right, par, vis);
          if(!vis[par[root]])
        ph= height(par[root] , par, vis);
    
    return  max(ph, max(lh,rh)) +1;
}

The final ans will be height-1;
