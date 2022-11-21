class Solution(object):
    def insertIntoBST(self, root, val):
        if root is None: return TreeNode(val)
        node = root
        while True:
            if val > node.val:  
                if node.right is not None:  
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    break
            else:  
                if node.left is not None:  
                    node = node.left
                else:  
                    node.left = TreeNode(val)
                    break
        return root