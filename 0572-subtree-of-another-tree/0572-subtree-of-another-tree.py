
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]

        while stack:
            node = stack.pop()

            if node.val==subRoot.val:
                if self.check(node, subRoot):
                    return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False

    def check(self, r:TreeNode, s:TreeNode) -> bool:
        stack = [(r, s)]

        while stack:
            node1, node2 = stack.pop()
            #print(node1, node2)
            if node1.val!=node2.val:
                return False
            if node1.left or node2.left:
                if (node1.left and not node2.left) or (not node1.left and node2.left):
                    return False    
                else:
                    stack.append((node1.left, node2.left))
            if node1.right or node2.right:
                if (node1.right and not node2.right) or (not node1.right and node2.right):
                    return False
                else:
                    stack.append((node1.right, node2.right))
        return True