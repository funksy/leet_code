def longestZigZag(root):
    if not root:
        return 0
    
    longest = 0
    stack = deque()
    
    if root.left:
        stack.append((root.left, 'l', 1))
    if root.right:
        stack.append((root.right, 'r', 1))
    
    while stack:
        node, prev_dir, depth = stack.popleft()
        longest= max(longest, depth)
        if prev_dir == 'l':
            if node.right:
                stack.append((node.right, 'r', depth + 1))
            if node.left:
                stack.append((node.left, 'l', 1))
        
        if prev_dir == 'r':
            if node.left:
                stack.append((node.left, 'l', depth + 1))
            if node.right:
                stack.append((node.right, 'r', 1))

    return longest