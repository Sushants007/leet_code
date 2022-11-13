class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ct=0
        while num1>=1 and num2>=1:   
            if num1>num2:
                num1=num1-num2
                ct+=1
            else:
                num2=num2-num1
                ct+=1
        return ct
