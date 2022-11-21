class FindElements:
    def __init__(self, root):
        self.A = A = set()

        if not root:
            return
        
        queue = collections.deque([[root,0]])
        while queue:
            n,x = queue.popleft()
            A.add(x)
            if n.left:
                queue.append( [n.left  , 2*x+1] )
            if n.right:
                queue.append( [n.right , 2*x+2] )
    
    def find(self, target):
        return target in self.A