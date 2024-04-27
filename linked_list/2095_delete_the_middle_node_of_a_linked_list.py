class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteMiddle(head):
    if head == None:
        return None
    
    prev = ListNode(0, head)
    slow = prev
    fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    slow.next = slow.next.next
    return prev.next


node3 = ListNode(4)
node2 = ListNode(3, node3)
node1 = ListNode(1, node2)

print(deleteMiddle(node1))