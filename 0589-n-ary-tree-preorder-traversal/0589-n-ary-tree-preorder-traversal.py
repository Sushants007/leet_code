class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        arr=[]
        self.dfs(root,arr)
        return arr
    def dfs(self, root, arr):
        if root is None:
            return None
        arr.append(root.val)
        for child in root.children:
            self.dfs(child,arr)
        
                