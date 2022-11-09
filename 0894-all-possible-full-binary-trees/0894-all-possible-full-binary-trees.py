# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    dp={}
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        
        #@lru_cache(None)
        def fn(n):
            
            if n == 1: 
                self.dp[n]=[TreeNode()]
                return self.dp[n]
            #if n%2==0:
            #    return []
            ans = []
            for nn in range(1, n, 2): 
                for left in fn(nn):
                    for right in fn(n-1-nn): 
                        ans.append(TreeNode(left=left, right=right))
            self.dp[n]=ans 
            return self.dp[n]
        
        return fn(N)