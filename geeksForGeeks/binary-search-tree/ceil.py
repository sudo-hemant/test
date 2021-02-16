
# iterative sol can be done using the same method as iterative floor

# recursive sol
class Store:
    def __init__(self):
        self.res = -1
    def update(self, value):
        self.res = value

def findCeil(root, inp):
    
    value = Store()
    
    def helper(curr, x):
        if not curr:
            return
        if curr.key == x:
            value.update(curr.key)
        elif curr.key < x:
            helper(curr.right, x)
        elif curr.key > x:
            value.update(curr.key)
            helper(curr.left, x)
    
    
    helper(root, inp)
    return value.res
