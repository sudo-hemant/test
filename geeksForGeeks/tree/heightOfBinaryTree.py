# iterative method to find height using queue

from collections import deque
def height(root):
    if not root:
        return 0
    height = 0
    q = deque()
    q.append(root)
    
    while q:
        length = len(q)
        for i in range(length):
            popped = q.popleft()
            if popped.left:
                q.append(popped.left)
            if popped.right:
                q.append(popped.right)
        height += 1

    return height

    