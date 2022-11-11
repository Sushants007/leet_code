class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ct=0
        count=0
        for i in range(len(s)):
            
            if s[i]=='R':
                count+=1
            else:
                count-=1
            if count==0 and i!=0:
                ct+=1
        return ct
            