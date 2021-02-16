
# iterative sol

def deleteNode(root, x):
    
    parent_found_at, found_at = search(root, x)
    
    if not found_at:
        return root
        
    if not found_at.left or not found_at.right:
        newCurr = None
        
        if not found_at.left:
            newCurr = found_at.right
        else:
            newCurr = found_at.left
        
        if not parent_found_at:
            return newCurr
            
        if parent_found_at.left == found_at:
            parent_found_at.left = newCurr
        else:
            parent_found_at.right = newCurr
            
    else:
        parent_successor, successor = inOrderSuccessor(found_at)
        
        if parent_successor:
            parent_successor.left = successor.right
        else:
            found_at.right = successor.right
        
        found_at.data = successor.data
        
    return root
    
    
def inOrderSuccessor(curr):
    prev = None
    curr = curr.right
    
    while curr.left:
        prev = curr
        curr = curr.left
    
    return prev, curr
    
    
def search(root, x):
    prev = None
    curr = root
    
    while curr and curr.data != x:
        prev = curr
        if curr.data < x:
            curr = curr.right
        else:
            curr = curr.left
            
    return prev, curr
