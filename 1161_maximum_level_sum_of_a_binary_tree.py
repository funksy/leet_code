def maxLevelSum(root):
    res = 1
    if not root:
        return res

    temp_sum = maxVal = root.val
    level = 1
    stack = deque([root])

    while stack:
        if temp_sum > maxVal:
            res = level
            maxVal = temp_sum
        
        nodes = len(stack)
        temp_sum = 0
        level += 1

        for i in range(nodes):
            node = stack.popleft()
            if node.left:
                stack.append(node.left)
                temp_sum += node.left.val
            if node.right:
                stack.append(node.right)
                temp_sum += node.right.val
    
    return res