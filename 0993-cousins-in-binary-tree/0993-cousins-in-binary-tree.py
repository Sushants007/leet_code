
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        dict={}
        tree=[]
        tree.append((root,0,0))
        while tree:
            node,parent,depth=tree.pop()
            if node:
                dict[node.val]=(parent,depth)
                tree.append((node.left,node.val,depth+1))
                tree.append((node.right,node.val,depth+1))
        return dict[x][1]==dict[y][1] and dict[x][0]!=dict[y][0]