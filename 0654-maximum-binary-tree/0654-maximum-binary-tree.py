class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        stack = []  
        for i in nums:
            node = TreeNode(i)
            lastpop = None
            
            while stack and stack[-1].val < i:  
                lastpop = stack.pop()
            node.left = lastpop
            
            if stack:
                stack[-1].right = node
            stack.append(node)
            
        return stack[0]