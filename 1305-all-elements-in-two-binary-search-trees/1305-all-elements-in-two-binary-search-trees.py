# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        arr=[]
        def dfs(node):
            if not node:
                return 0
            arr.append(node.val)

            dfs(node.left)
            dfs(node.right)
        dfs(root1)
        dfs(root2)
        print(arr)
        return sorted(arr)
            