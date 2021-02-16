
# recursive sol
class BST:
    def search(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1
        if data < node.data:
            return self.search(node.left, data)
        if data > node.data:
            return self.search(node.right, data)


# iterative sol
from collections import deque
class BST:
    def search(self, node, data):
        q = deque()
        q.append(node)
        while q:
            popped = q.popleft()
            if data == popped.data:
                return True
            if data < popped.data:
                if popped.left:
                    q.append(popped.left)
                else:
                    return 0
            else:
                if popped.right:
                    q.append(popped.right)
                else:
                    return 0
