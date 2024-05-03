def pathSum(root):
    if not root:
        return 0

    count = 0
    stack = [root]

    while stack:
        node = stack.pop()
        count = self.pathSumFromSource(node, count, targetSum)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    
    return count
    
def pathSumFromSource(self, root, count, targetSum):
    if not root:
        return False

    stack = [(root, root.val)]
    while stack:
        node, total = stack.pop()
        if total == targetSum:
            count += 1
        if node.right:
            stack.append((node.right, total + node.right.val))
        if node.left:
            stack.append((node.left, total + node.left.val))
        
    return count