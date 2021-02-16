# iterative solution for checking if sum of its children is equal to the parent

def isSumProperty(root):
    if not root:
        return 1
    
    q = []
    q.append(root)

    while q:
        popped = q.pop()
        l, r = 0, 0
        if popped.left:
            l = popped.left.data
            q.append(popped.left)
        if popped.right:
            r = popped.right.data
            q.append(popped.right)
        
        if not popped.left and not popped.right:
            continue
        if (l + r) != popped.data:
            return 0
    
    return 1
