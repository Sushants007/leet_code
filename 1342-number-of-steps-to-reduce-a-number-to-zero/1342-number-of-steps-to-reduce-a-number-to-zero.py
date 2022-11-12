class Solution:
    def numberOfSteps(self, n: int) -> int:
        ct=0
        while n>=1:    
            if n%2==0:
                n=n//2
                ct+=1
            else:
                n-=1
                ct+=1
        return ct