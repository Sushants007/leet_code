class Solution:
    def sumEvenGrandparent(self, node: TreeNode) -> int:
        self.total = 0
        
        def dfs(root):
            if root.val % 2 == 0:
                if root.left:
                    if root.left.left:
                        self.total += root.left.left.val 
                    if root.left.right:
                        self.total += root.left.right.val
                if root.right:
                    if root.right.left:
                        self.total += root.right.left.val
                    if root.right.right:
                        self.total += root.right.right.val
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            return
        
        dfs(node)
        return self.total