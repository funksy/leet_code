def goodNodes(root):
    if not root:
        return 0

    nodes = [(root, root.val)]
    count = 0
    while nodes:
        node, max_val = nodes.pop()
        if node.val >= max_val:
            count += 1
        max_val = max(node.val, max_val)
        if node.left:
            nodes.append((node.left, max_val))
        if node.right:
            nodes.append((node.right, max_val))
    
    return count