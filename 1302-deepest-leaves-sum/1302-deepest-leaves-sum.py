class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        while queue:
            curr = 0
            for i in range(len(queue)):
                node = queue.pop(0)
                curr = curr + node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return curr
