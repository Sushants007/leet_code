class Solution:
    def numberOfMatches(self, n: int) -> int:
        count=0
        for i in range(n):
            if n%2==0:
                n=n//2
                count+=1
            else:
                n=((n-1)/2)+1
                count+=1
        return count-1