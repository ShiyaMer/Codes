#User function Template for python3

'''
heap = [0 for i in range(101)]  # our heap to be used
'''
#Function to insert a value in Heap.
def parent(i):
    return (i-1)//2
def left(i):
    return (2*i)+1
def right(i):
    return (2*i)+2
def minheapify(p):
    global curr_size
    smallest=p
    lef=left(p)
    rig=right(p)
    if lef<curr_size and heap[lef]<heap[smallest]:
        smallest=lef
    if rig<curr_size and heap[rig]<heap[smallest]:
        smallest=rig
    if smallest!=p:
        heap[p],heap[smallest]=heap[smallest],heap[p]
        minheapify(smallest)
    
def insertKey (x):
    global curr_size
    if curr_size>=len(heap):
        return 
    curr_size+=1
    heap[curr_size-1]=x
    cur=curr_size-1
    while(cur!=0 and heap[cur]<heap[parent(cur)]):
        heap[cur],heap[parent(cur)]=heap[parent(cur)],heap[cur]
        cur=parent(cur)
    


def deleteKey (i):
    global curr_size
    if i>=curr_size:
        return 
    heap[i]=heap[curr_size-1]
    curr_size-=1
    for i in range(curr_size//2,-1,-1):
        minheapify(i)
    
#Function to extract minimum value in heap and then to store 
#next minimum value at first index.
def extractMin ():
    global curr_size
    if curr_size==0:
        return -1
    min=heap[0]
    heap[0]=heap[curr_size-1]
    curr_size-=1
    minheapify(0)
    return min
    
    

