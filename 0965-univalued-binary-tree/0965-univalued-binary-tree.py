# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root) -> bool:
        x=root.val
        q=[root]
        while q:
            node=q.pop(0)
            if node.val!=x:
                return False
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return True