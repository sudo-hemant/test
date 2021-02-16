# iterative method using level order traversal which uses queue ds

from collections import deque
def isIdentical(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    q1 = deque()
    q2 = deque()
    q1.append(root1)
    q2.append(root2)
    
    while q1 and q2:
        r1 = q1.pop()
        r2 = q2.pop()
        if r1.data != r2.data:
            return False
        
        if r1.left and r2.left:
            q1.append(r1.left)
            q2.append(r2.left)
        elif r1.left or r2.left:
            return False
        
        if r1.right and r2.right:
            q1.append(r2.right)
            q2.append(r2.right)
        elif r1.right or r2.right:
            return False
    
    return True    
