from collections import deque
def preorder(root):
    if not root:
        return []
    q = deque()
    ans = []
    q.append(root)
    
    while q:
        curr = q.pop()
        ans.append(curr.data)
        if curr.right: q.append(curr.right)
        if curr.left: q.append(curr.left)
        
    return ans
