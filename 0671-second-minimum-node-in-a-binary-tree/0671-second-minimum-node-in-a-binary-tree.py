class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        nums = []
        nodes = [root]
        while nodes:
            t = nodes.pop()
            nums.append(t.val)
            if t.left:
                nodes.append(t.left)
            if t.right:
                nodes.append(t.right)
        
        if len(set(nums)) == 1:
            return -1
        
        return sorted(set(nums))[1]