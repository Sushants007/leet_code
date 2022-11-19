# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        q=[(root,False)]
        ans=0
        while q:
            cur,isLeft=q.pop()
            if not cur.left and not cur.right and isLeft:
                ans+=cur.val
            if cur.right:
                q.append((cur.right,False))
            if cur.left:
                q.append((cur.left,True))
        return ans
                