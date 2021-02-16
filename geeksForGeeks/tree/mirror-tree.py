# construct mirror tree using recursion

def mirror(root):
    
    mirrorUtil(root)
    
    
def mirrorUtil(curr):
    
    if not curr:
        return 

    left = curr.left
    right = curr.right
    curr.left = right
    curr.right = left
    
    mirrorUtil(curr.left)
    mirrorUtil(curr.right)


# -------------------------------------------------------------------------------


# iterative solution

from collections import deque
def mirror(root):
    queue = deque()
    queue.append(root)
    
    while queue:
        popped = queue.popleft()
        
        left = popped.left
        right = popped.right
        
        popped.left = right
        popped.right = left
        
        if popped.left:
            queue.append(popped.left)
        if popped.right:
            queue.append(popped.right)
    
