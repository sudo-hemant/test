
# recursive inorder traversal

def printNearNodes(root, low, high):
    
    res = []
    
    def helper(curr, low, high, res):
        if not curr:
            return
        
        helper(curr.left, low, high, res)
        
        if low <= curr.data <= high:
            res.append(curr.data)
        
        helper(curr.right, low, high, res)
        
        
    helper(root, low, high, res)
    
    return res
