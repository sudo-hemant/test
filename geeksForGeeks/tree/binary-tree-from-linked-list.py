# using level order traversal

from collections import deque
def convert(head):
    if not head:
        return head
    q = deque()
    new_head = Tree(head.data)
    q.append(new_head)
    curr = head
    
    while q:
        popped = q.popleft()
        if curr.next:
            new = Tree(curr.next.data)
            popped.left = new
            q.append(new)
            curr = curr.next
        if curr.next:
            new = Tree(curr.next.data)
            popped.right = new
            q.append(new)
            curr = curr.next
    
    return new_head
