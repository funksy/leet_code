from collections import deque

def lowestCommonAncestor(root, p, q):
    stack = deque([root])
    parent = {root: None}

    while stack:
        node = stack.popleft()

        if node.left:
            stack.append(node.left)
            parent[node.left] = node
        
        if node.right:
            stack.append(node.right)
            parent[node.right] = node
        
        if p in parent and q in parent:
            break
    
    ancestors = set()
    while p:
        ancestors.add(p)
        p = parent[p]
    
    while q:
        if q in ancestors:
            return q
        q = parent[q]