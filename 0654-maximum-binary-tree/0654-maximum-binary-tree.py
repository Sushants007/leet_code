class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(nums):
            if not nums:
                return None
            maxi=max(nums)
            index=nums.index(maxi)
            root=TreeNode(maxi)
            root.left=dfs(nums[:index])
            root.right=dfs(nums[index+1:])
            return root
        return dfs(nums)