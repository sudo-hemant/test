
# this can be written in much better way

# recursive sol

class Store:
    def __init__(self):
        self.res = float('inf')
    def update(self, value):
        self.res = value
        
def minDiff(root, k):
    
    value = Store()
    
    def helper(curr, x):
        if not curr:
            return
        
        if curr.data == x:
            value.update(0)
        elif curr.data < x:
            value.update(min(value.res, abs(x - curr.data)))
            helper(curr.right, x)
        elif curr.data > x:
            value.update(min(value.res, abs(curr.data - x)))
            helper(curr.left, x)
        
    helper(root, k)
    
    return value.res
