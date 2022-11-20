class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False
        queue = [(root, sum-root.val)]
        while queue:
            curr, val = queue.pop(0)
            if not curr.left and not curr.right and val == 0:
                return True
            if curr.left:
                queue.append((curr.left, val-curr.left.val))
            if curr.right:
                queue.append((curr.right, val-curr.right.val))
        return False