class FindElements(object):
    def __init__(self, root):
        self.A = A = set()
        #
        def recover(n,x):
            if n:
                A.add(x)
                recover(n.left , 2*x + 1)
                recover(n.right, 2*x + 2)
        #
        recover(root,0)
    #
    def find(self, target):
        return target in self.A