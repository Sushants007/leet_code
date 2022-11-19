# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res=[]
        q=[(root,'')]
        while q:
            node,ans=q.pop()
            if not node.left and not node.right:
                res.append(ans+str(node.val))
            if node.left:
                q.append((node.left,ans+str(node.val)+'->'))
            if node.right:
                q.append((node.right,ans+str(node.val)+'->'))
        return res