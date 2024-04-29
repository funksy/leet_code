def pairSum(head):
    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    
    curr, prev = slow, None
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    
    max_sum = 0
    while prev:
        max_sum = max(max_sum, head.val + prev.val)
        prev = prev.next
        head = head.next
    
    return max_sum