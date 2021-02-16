# using recursion 

def isBalanced(root):
    
    def check(curr):
        
        if not curr:
            return 0
        if not curr.left and not curr.right:
            return 1
            
        left_height = check(curr.left)
        if left_height == -1:
            return -1
        
        right_height = check(curr.right)
        if right_height == -1:
            return -1
            
        if abs(left_height - right_height) > 1:
            return -1
        
        return max(left_height, right_height) + 1
        
    return False if check(root) == -1 else True
