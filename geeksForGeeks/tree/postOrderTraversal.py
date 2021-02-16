# iterative post order traversal using 2 stacks!

# HINT : we are iterating the tree in reverse order of our final output 
# and pushing it into the second stack which stores our ans
from collections import deque
def postOrder(root):
    if not root:
        return []
        
    s_1 = deque()
    s_2 = deque()
    ans = []
    s_1.append(root)
    while s_1:
        popped = s_1.pop()
        s_2.append(popped.data)
        
        if popped.left:
            s_1.append(popped.left)
        if popped.right:
            s_1.append(popped.right)
            
    while s_2:
        ans.append(s_2.pop())
    
    return ans