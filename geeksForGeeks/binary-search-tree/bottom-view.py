
# using iterative level order traversal 


from collections import deque

def bottomView(root):
    
    mp = {}
    res = []
    q = deque()
    minn, maxx = 0, 0
    
    q.append((root, 0))
    
    while q:
        node, index = q.popleft()
        minn, maxx = min(minn, index), max(maxx, index)
        
        mp[index] = node.data
        
        if node.left:
            q.append((node.left, index - 1))
        if node.right:
            q.append((node.right, index + 1))

    for i in range(minn, maxx + 1):
        res.append(mp[i])
    
    return res
