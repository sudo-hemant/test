
# recursive method


def maxDiff(root):

    class Variable:
        def __init__(self):
            self.result = float('-inf')
        
        def update(self, result):
            self.result = result
            
    update_values = Variable()
    
    def helper(curr):
        if not curr:
            return float('inf')
        if not curr.left and not curr.right:
            return curr.data
        
        
        left_value = helper(curr.left)
        right_value = helper(curr.right)
        
        min_value = min(left_value, right_value)
        update_values.result = max(curr.data - min_value, update_values.result)
        
        return min(min_value, curr.data)
        
    helper(root)
    return update_values.result
