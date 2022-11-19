class Solution: 
    def isCousins(self, root, x, y):
        def dept(node, d, par):
            if not node: return 
			
            if node.val == x:
                self.a = d
                self.aparent= par
	
            elif node.val == y:
                self.b = d
                self.bparent= par
            dept(node.left, d+1, node)
            dept(node.right, d+1, node)
        dept(root, 0, None)
        # return True if a and b are equal and their parents are not same
        return self.a == self.b and self.aparent != self.bparent