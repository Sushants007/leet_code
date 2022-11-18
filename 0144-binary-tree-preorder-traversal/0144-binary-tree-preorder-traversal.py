
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        q=[root]
        while q:
            node= q.pop()
            if node:
                res.append(node.val)
                q.append(node.right)
                q.append(node.left)
        return res
