
#  important problem

# recursive method
class Store:
    def __init__(self, max_curve, result):
        self.max_curve = max_curve
        self.result = result
        
    def update(self, max_curve, result):
        self.max_curve = max_curve
        self.result = result
        

def findMaxSum(root): 

    if not root:
        return 0
        
    update_values = Store(0, float('-inf'))
    
    def helper(curr):
        if not curr:
            return 0
        left_value = helper(curr.left)
        right_value = helper(curr.right)
        
        max_straight = max(max(left_value, right_value) + curr.data, curr.data)
        max_curve = max(max_straight, left_value + right_value + curr.data)
        result = max(update_values.result, max_curve)
        
        update_values.update(max_curve, result)
        return max_straight
    
    helper(root)
    return update_values.result
