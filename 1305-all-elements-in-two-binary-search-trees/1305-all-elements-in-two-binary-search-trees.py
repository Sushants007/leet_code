
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        arr=[]
        def dfs(node):
            nonlocal arr
            if not node:
                return 0
            arr.append(node.val)

            dfs(node.left)
            dfs(node.right)
        dfs(root1)
        dfs(root2)
        print(arr)
        return sorted(arr)
            