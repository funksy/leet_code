def rightSideView(root):
    res = []
    if not root:
        return res

    stack = deque([root]) #using a deque so we can popleft()

    while stack:
        res.append(stack[-1].val) #grabbing the right most value at the current level
        nodes = len(stack)
        for i in range(nodes): #iterating through all nodes at the current level
            node = stack.popleft()  #starting at the left so that the rightmost value is the last value in the stack after iterating
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
    
    return res