
# recursive method usign preorder traversal


def serialize(root, A):
    if not root:
        A.append(-1)
        return 
    A.append(root.data)
    serialize(root.left, A)
    serialize(root.right, A)
    
        
class Store:
    def __init__(self):
        self.index = 0
    
    def update(self):
        self.index += 1
    
    
def deSerializerUtil(A, values):
    # bcos when the value is -1 which means its not node but its parent is pointing to None 
    # and the other condition is bcos when we reach end we want to return 
    if values.index == len(A) or A[values.index] == -1:
        values.update()
        return None
    
    curr = Node(A[values.index])
    values.update()
    curr.left = deSerializerUtil(A, values)
    curr.right = deSerializerUtil(A, values)
    
    return curr

    
def deSerialize(A):
    values = Store()
    return deSerializerUtil(A, values)
