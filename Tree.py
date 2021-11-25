class Node:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None
    
def insert(temp,key):
    if not temp:
        root = Node(key)
        return
    
    q= []
    q.append(temp)
    while len(q):
        temp = q[0]
        q.pop(0)

        if not temp.left:
            temp.left = Node(key)
            break
        else:
            q.append(temp.left)
        
        if not temp.right:
            temp.right = Node(key)
            break
        else:
            q.append(temp.right)

def deepestdlt(root,d_node):
    q =[]
    q.append(root)
    while len(q):
        temp = q.pop(0)
        if temp is d_node:
            temp = None
            return
        if temp.right:
            if temp.right is d_node:
                temp.right = None
                return
            else:
                q.append(temp.right)
        
        if temp.left:
            if  temp.left is d_node:
                temp.left = None
                return
            else:
                q.append(temp.left)



def deletion(root,key):
    if root==None:
        return
    if root.left==None and root.right==None:
        if root.val ==key:
            return None
        else:
            return root
    
    key_node = None
    q =[]
    q.append(root)
    while len(q):
        temp = q.pop(0)
        if temp.val==key:
            key_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    
    if key_node:
        x = temp.val
        deepestdlt(root,temp)
        key_node.val = x
    
    return root
        
def inorder(temp):
    if not temp:
        return
    
    inorder(temp.left)
    print(temp.val,end=" ")
    inorder(temp.right)

def BFS(root):
    if root is None:
        return
    
    q =[]
    q.append(root)
    while len(q):
        print(q[0].val)
        node = q.pop(0)

        if node.left is not None:
            q.append(node.left)
        
        if node.right is not None:
            q.append(node.right)
            

if __name__ == '__main__':
    root = Node(10)
    arr = [23,2,54,67,89,12]
    for i in range(len(arr)):
        insert(root,arr[i])
    #inorder(root)
    #print("\n")
    #deletion(root,54)
    #inorder(root)
    BFS(root)
