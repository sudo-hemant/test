from collections import deque
def InOrder(root):
    if not root:
        return []
    ans = []
    s = deque()
    curr = root
    
    while s or curr:
        if curr:
            s.append(curr)
            curr = curr.left
        else:
            popped = s.pop()        # is it pop or popleft() ? 
            ans.append(popped.data)
            curr = popped.right

    return ans