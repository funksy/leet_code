class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEvenList(head):
    if not head:
        return head
    
    odd = head
    even = head.next
    even_head = even
    while(even and even.next):
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = even_head
    return head


node3 = ListNode(4)
node2 = ListNode(3, node3)
node1 = ListNode(1, node2)

print(oddEvenList(node1))