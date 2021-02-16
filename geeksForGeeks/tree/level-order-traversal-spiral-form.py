# spiral order traversal using 1 queue and 1 stack 

from collections import deque
def printSpiral(root):
    if not root:
        return []

    ans = []
    q = deque()
    s = deque()
    q.append(root)
    reverse = True

    while q:
        length = len(q)
        
        for i in range(length):
            popped = q.popleft()

            if reverse:
                s.append(popped.data)
            else:
                ans.append(popped.data)
            
            if popped.left:
                q.append(popped.left)
            if popped.right:
                q.append(popped.right)
                
        while s:
            ans.append(s.pop())
        
        reverse = not reverse
    
    for element in ans:
        print(element, end=" ")
