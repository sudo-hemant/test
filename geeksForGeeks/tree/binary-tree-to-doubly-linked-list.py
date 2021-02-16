# using inorder traversal approach and keeping track of prev node

global prev
global head

def bToDLL(root):
    global prev
    global head
    head = None
    prev = None
    
    
    def helper(curr):
        global prev
        global head
        
        if not curr:
            return None
        
        helper(curr.left)
        
        if prev == None:
            head = curr
        else:
            curr.left = prev
            prev.right = curr
        prev = curr
        
        helper(curr.right)


    helper(root)
    return head

