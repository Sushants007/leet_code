class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans=[]
        if root==None:
            return ans
        q=[]
        q.append(root)
        while q:
            level=[]
            n=len(q)
            for i in range(0,n,1):
                node=q.pop(0)
                # q.remove(q[0])
                level.append(node.val)
                if node.left !=None:
                    q.append(node.left)
                if node.right!=None:
                    q.append(node.right)
            ans.append(level)
        return ans