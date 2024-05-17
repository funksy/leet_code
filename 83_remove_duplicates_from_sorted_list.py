def deleteDuplicates(head):
    if head == None:
            return head

    current = head
    
    while current.next:
        if current.next.val == current.val:
            current.next = current.next.next
        else:
            current = current.next

    return head