class MinStack:

    def __init__(self):
        self.stack=[]
        self.minele=sys.maxsize

    def push(self, x: int) -> None:
        if len(self.stack)==0:
            self.stack.append(x)
            self.minele=x
        else:
            if x>=self.minele:
                self.stack.append(x)
            elif x<self.minele:
                self.stack.append(2*x-self.minele)
                self.minele=x

    def pop(self) -> None:
        if self.stack==0:
            return -1
        else:
            if self.stack[-1]>=self.minele:
                self.stack.pop()
            elif self.stack[-1]<self.minele:
                self.minele=2*self.minele-self.stack[-1]
                self.stack.pop()

    def top(self) -> int:
        if len(self.stack)==0:
            return -1
        else:
            if self.stack[-1]>=self.minele:
                return self.stack[-1]
            elif self.stack[-1]<self.minele:
                return self.minele
        
        
    def getMin(self) -> int:
        if self.stack==0:
            return -1
        return self.minele
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()