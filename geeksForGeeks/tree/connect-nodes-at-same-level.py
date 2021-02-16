
# iterative sol using level order traversal


from collections import deque

def connect(root):

    if not root:
        return root
        
    q = deque()
    q.append(root)

    while q:
        length = len(q)
        for i in range(length):
            popped = q.popleft()
            
            if i + 1 == length:
                popped.nextRight = None
            else:
                popped.nextRight = q[0]
            
            if popped.left:
                q.append(popped.left)
            if popped.right:
                q.append(popped.right)
        