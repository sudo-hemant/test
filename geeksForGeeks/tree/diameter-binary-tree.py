# the code can be better by using a global variable insted of an array to store diameter
# here array is taken bcos it is passed by reference and unmutable variables are passed by value

def diameter(root):
    
    max_diameter = [0]
    calculate(root, max_diameter)
    return max_diameter[0] 
    
    
def calculate(root, max_diameter):
    if not root:
        return 0
    
    left_height = calculate(root.left, max_diameter)
    right_height = calculate(root.right, max_diameter)
    
    max_diameter[0] = max(max_diameter[0], left_height + right_height + 1)
    return max(left_height, right_height) + 1
