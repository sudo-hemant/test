

# iterative traversal using 

def printCommon(root1, root2):

    stack1 = []
    stack2 = []
    
    res = []
    while True:
        if root1:
            stack1.append(root1)
            root1 = root1.left
        elif root2:
            stack2.append(root2)
            root2 = root2.left
        elif stack1 and stack2:
            root1 = stack1[-1]
            root2 = stack2[-1]
            if root1.data == root2.data:
                res.append(root1.data)
                stack1.pop()
                stack2.pop()
                root1 = root1.right
                root2 = root2.right
            elif root1.data < root2.data:
                stack1.pop()
                root1 = root1.right
                # setting this to none bcos we want this no to point to other node
                root2 = None
            elif roota.data > root2.data:
                stack2.pop()
                root1 = None
                root2 = root2.right
        else:
            break
    
    return res    
