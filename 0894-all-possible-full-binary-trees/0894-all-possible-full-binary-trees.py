# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        
        #@lru_cache(None)
        def fn(n):
            
            if n == 1: return [TreeNode()]
            #if n%2==0:
            #    return []
            ans = []
            for nn in range(1, n, 2): 
                for left in fn(nn):
                    for right in fn(n-1-nn): 
                        ans.append(TreeNode(left=left, right=right))
            return ans 
        
        return fn(N)