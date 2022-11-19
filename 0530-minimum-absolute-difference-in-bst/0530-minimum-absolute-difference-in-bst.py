class Solution:
    pre = -float('inf')
    res = float('inf')
    
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        if root.left:
            self.getMinimumDifference(root.left)
        self.res = min(self.res, root.val - self.pre)
        self.pre = root.val
        if root.right:
            self.getMinimumDifference(root.right)
        return self.res