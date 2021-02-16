

# iterative sol using level order traversal

from collections import deque

def topView(root):

    minn, maxx = 0, 0
    mp = {}
    q = deque()
    q.append((root, 0))
    
    while q:
        node, index = q.popleft()
        minn, maxx = min(minn, index), max(maxx, index)
        
        if index not in mp:
            mp[index] = node.data
            
        if node.left:
            q.append((node.left, index - 1))
        if node.right:
            q.append((node.right, index + 1))
            
    for i in range(minn, maxx + 1):
        print(mp[i], end=" ")
