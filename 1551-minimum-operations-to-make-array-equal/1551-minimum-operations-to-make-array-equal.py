class Solution:
    def minOperations(self, n: int) -> int:
        
        if n==1:return 0
        else:
            a=1 
            b=2*(n-1)+1 
            avg=(b+1)//2  
            res=0 
            for i in range(n//2,n): 
                res+=abs((2*i+1)-avg)   
            return res