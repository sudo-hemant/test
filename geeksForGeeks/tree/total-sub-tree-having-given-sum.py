



def countSubtreesWithSumX(root, X):

    class Store:
        def __init__(self):
            self.result = 0
            
        def update(self):
            self.result += 1

    values = Store()

    def helper(curr, find):
        if not curr:
            return 0
        
        left_value = helper(curr.left, find)
        right_value = helper(curr.right, find)
        
        summ = left_value + right_value + curr.data
        if summ == find:
            values.update()
        
        return summ
        
    helper(root, X)
    return values.result
