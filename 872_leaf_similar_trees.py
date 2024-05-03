def leafSimilar(root1, root2):
    def listOfLeafs(root):
        if not root:
            return []
        
        if not root.left and not root.right:
            return [root.val]

        return listOfLeafs(root.left) + listOfLeafs(root.right)
    return listOfLeafs(root1) == listOfLeafs(root2)