class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return []
        
        queue = [root]
        curr = 1
        while queue:
            if curr == -1:
                l = 0
                r = len(queue) - 1
                
                while l <= r:
                    queue[l].val, queue[r].val = queue[r].val, queue[l].val
                    l += 1
                    r -= 1
            curr *= (-1)
                
                  
            for _ in range(len(queue)):
                ele = queue.pop(0)
                
                if ele.left:
                    queue.append(ele.left)
                    queue.append(ele.right)
                    
        return root