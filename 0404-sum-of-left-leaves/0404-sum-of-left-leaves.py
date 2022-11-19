class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        q, ans = deque([(root, False)]), 0
        while q:
            cur, isLeft = q.popleft()
            if not cur.left and not cur.right and isLeft:
                ans = ans + cur.val
            if cur.right:
                q.append((cur.right, False))
            if cur.left: 
                q.append((cur.left, True))
        return ans