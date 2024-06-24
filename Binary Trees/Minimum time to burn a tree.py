if not root and  not target:
            return 0
        q0=[root]
        d={root:None}
        while(q0):
            i=len(q0)
            for _ in range(i):
                n=q0.pop(0)
                if n.left:
                    d[n.left]=n
                    q0.append(n.left)
                if n.right:
                    d[n.right]=n
                    q0.append(n.right)
        visited=[]
        q=[target]
        dis=0
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
