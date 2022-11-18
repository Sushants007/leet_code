class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
       
        res = []     
        startnode = None
        prev = None
        lastnode = None
        
        def dfs(root):
            nonlocal res, startnode, prev, lastnode
            if not root:
                return 
            dfs(root.left)
			
          
            if prev and prev.val > root.val:
                if not startnode:
                    startnode = prev
                lastnode = root
                
            prev = root
            dfs(root.right)
            
        
        dfs(root)
        if startnode and lastnode:
            startnode.val, lastnode.val = lastnode.val, startnode.val