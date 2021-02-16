# level order traversal using a queue

from collections import deque
def levelOrder( root ):
    if not root:
        return []
    ans = []
    q = deque()
    q.append(root)

    while q:
        popped = q.popleft()
        ans.append(popped.data)
        if popped.left:
            q.append(popped.left)
        if popped.right:
            q.append(popped.right)
            
    return ans