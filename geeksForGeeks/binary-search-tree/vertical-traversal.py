
# using iterative level order traversal

from collections import deque
def verticalOrder(root): 
    
    minn, maxx = 0, 0
    mp = {}
    q = deque()
    q.append((root, 0))
    
    while q:
        node, index = q.popleft()
        
        minn, maxx = min(index, minn), max(index, maxx)
        
        if index in mp:
            mp[index].append(node.data)
        else:
            mp[index] = [node.data]
        
        if node.left:
            q.append((node.left, index - 1))
        if node.right:
            q.append((node.right, index + 1))
            
    res = []
    for i in range(minn, maxx + 1):
        res.extend(mp[i])
    
    return res
