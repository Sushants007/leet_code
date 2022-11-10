"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        out=[]
        self.dfs(root,out)
        return out
    def dfs(self,root,out):
        if root is None:
            return None
        out.append(root.val)
        for child in root.children:
            self.dfs(child,out)
        
                