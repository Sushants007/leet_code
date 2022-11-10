"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        out=[]
        
        if root is None:
            return out       
        self.dfs(root,out)          
        return out
    def dfs(self,root,out):

        
        for child in root.children:
            self.dfs(child,out)
        out.append(root.val)