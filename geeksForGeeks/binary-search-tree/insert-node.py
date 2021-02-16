

# recursive sol
def insert(root, key):
    
    if root.data == key:
        return root
    
    
    if key < root.data:
        if root.left:
            insert(root.left, key)
        else:
            root.left = Node(key)
    if key > root.data:
        if root.right:
            insert(root.right, key)
        else:
            root.right = Node(key)


# iterative sol
from collections import deque

def insert(root, key):
    
    q = deque()
    q.append(root)
    
    while q:
        popped = q.popleft()
        if popped.data == key:
            break
        if key < popped.data:
            if popped.left:
                q.append(popped.left)
            else:
                popped.left = Node(key)
                break
        else:
            if popped.right:
                q.append(popped.right)
            else:
                popped.right = Node(key)
                break
    
    return root
