class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf_seq_1 = []
        leaf_seq_2 = []

        
        def helper( node: TreeNode, container):
            
            if node:
                
                helper( node.left, container )
                
                if not node.left and not node.right:
                    container.append( node.val )
                    
                helper( node.right, container )
                
        helper( root1, leaf_seq_1)
        helper( root2, leaf_seq_2)
        
        return leaf_seq_1 == leaf_seq_2