def searchBST(root, val):
    while(root):
        if root.val == val:
            return root
        if root.val < val:
            root = root.right
        else:
            root = root.left
    return None