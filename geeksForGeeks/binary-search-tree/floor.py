


# recursive sol
class Store:
    def __init__(self):
        self.res = -1
    def update(self, value):
        self.res = value

def floor(root,x):
    value = Store()
    
    def helper(curr, x):
        if not curr:
            return 
        if curr.data == x:
            value.update(x)
            return
        elif curr.data > x:
            helper(curr.left, x)
        elif curr.data < x:
            value.update(curr.data)
            helper(curr.right, x)

    helper(root, x)
    return value.res



# iterative sol
from collections import deque

def floor(root,x):
        
    q = deque()
    q.append(root)
    res = -1
    
    while q:
        popped = q.popleft()
        if popped.data == x:
            res = popped.data
            return res
        elif popped.data > x:
            if popped.left:
                q.append(popped.left)
            else:
                return res
        elif popped.data < x:
            res = popped.data
            if popped.right:
                q.append(popped.right)
            else:
                return res

