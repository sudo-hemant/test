
# do its iterative solution as well

# recursive
def inOrder(root):
    
    if not root:
        return []
    inorder = []
    
    
    def helper(curr, inorder):
        if not curr:
            return
        helper(curr.left, inorder)
        inorder.append(curr.data)
        helper(curr.right, inorder)
        
    
    helper(root, inorder)
    return inorder
