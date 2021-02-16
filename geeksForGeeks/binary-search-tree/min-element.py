
from collections import deque

# iterative solution
def minValue(root):
    q = deque()
    q.append(root)
    
    while q:
        popped = q.popleft()
        if popped.left:
            q.append(popped.left)
        else:
            return popped.data
