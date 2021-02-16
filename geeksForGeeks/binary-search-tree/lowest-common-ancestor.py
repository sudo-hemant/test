



def LCA(root, n1, n2):
    
    if not root:
        return
    
    if root.data > max(n1, n2):
        return LCA(root.left, n1, n2)
    
    elif root.data < min(n1, n2):
        return LCA(root.right, n1, n2)
    
    #  THIS is handling all the left cases bcos if we can't move left or right, then there is two possibility 
    #  that the current node which is to be found or is either one of the node or it is the node which have
    #  those two nodes in both side
    return root
