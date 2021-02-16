# using level order traversal method and printing element when we are at the starting of level

from collections import deque
def LeftView(root):
    if not root:
        return []

    queue = deque()
    queue.append(root)
    ans = []
    
    while queue:
        length = len(queue)
        
        for i in range(length):
            popped = queue.popleft()
            
            if i == 0:
                ans.append(popped.data)
            
            if popped.left:
                queue.append(popped.left)
            if popped.right:
                queue.append(popped.right)

    return ans
