


# recursive sol using inorder traversal

class Store:
    def __init__(self):
        self.prev = float('-inf')
    def update(self, value):
        self.prev = value
        
def isBST(root):
    
    value = Store()
    
    def helper(curr):
        if not curr:
            return True
        
        if not helper(curr.left):
            return False
        
        if curr.data <= value.prev:
            return False
        value.update(curr.data)
        
        return helper(curr.right)
        
    return helper(root)
    

# 2nd method -- we can have range for every left child and right child