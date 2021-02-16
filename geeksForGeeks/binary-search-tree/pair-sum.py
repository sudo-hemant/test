

# can be done using iterative as well

# recursive sol using inorder traversal,
def findPair(root,x):
    
    st = set()
    
    def helper(curr, st, x):
        if not curr:
            return False
            
        if helper(curr.left, st, x):
            return True
        
        if x - curr.key in st:
            return True
        st.add(curr.key)
        
        return helper(curr.right, st, x)
        
    
    return helper(root, st, x)