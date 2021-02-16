# to check if it is foldable from b/w 

# recursive solution
def IsFoldable(root):
    
    if not root:
        return True
    
    def helper(curr1, curr2):
        if not curr1 and not curr2:
            return True
        if not curr1 or not curr2:
            return False
            
        return helper(curr1.left, curr2.right) and helper(curr1.right, curr2.left)
        
        
    ans = helper(root.left, root.right)
    return ans


# -----------------------------------------------------------------------------------------------------


# iterative method using level order traversal
from collections import deque
def IsFoldable(root):
    
    if not root:
        return True
    
    if not root.left and not root.right:
        return True
        
    if not root.left or not root.right:
        return False
        
    q = deque()
    q.append(root.left)
    q.append(root.right)
    
    while q:
        left_node = q.popleft()
        right_node = q.popleft()
        
        if left_node.left and right_node.right: 
            q.append(left_node.left)
            q.append(right_node.right)
        elif left_node.left or right_node.right:
            return False
        
        if left_node.right and right_node.left:
            q.append(left_node.right)
            q.append(right_node.left)
        elif left_node.right or right_node.left:
            return False
            
    return True
        
        