class Solution:
	def balanceBST(self, root: TreeNode) -> TreeNode:
		arr = []
		def dfs(node):
			if node:
				dfs(node.left)
				arr.append(node.val)
				dfs(node.right)
		dfs(root)

		def bst(nums):
			if not nums:
				return None
			mid = len(nums) // 2
			root = TreeNode(nums[mid])
			root.left = bst(nums[:mid])
			root.right = bst(nums[mid + 1:])
			return root

		return bst(arr)