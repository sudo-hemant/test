# either both are present or none is present

def lca(root, n1, n2):
    
    if not root:
        return None
    if root.data in (n1, n2):
        return root
        
    left = lca(root.left, n1, n2)
    right = lca(root.right, n1, n2)
    
    if left and right:
        return root
        
    if left:
        return left
    if right:
        return right
        
    return None
