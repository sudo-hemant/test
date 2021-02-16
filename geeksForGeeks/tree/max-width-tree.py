# using 1 queue that uses the level order traversal approach

from collections import deque
def getMaxWidth(root):
    
    max_width = 0
    queue = deque()
    
    if not root:
        return max_width
    queue.append(root)    
    
    while queue:
        length = len(queue)
        max_width = max(max_width, length)
        
        for i in range(length):
            popped = queue.popleft()
            if popped.left:
                queue.append(popped.left)
            if popped.right:
                queue.append(popped.right)
    
    return max_width
