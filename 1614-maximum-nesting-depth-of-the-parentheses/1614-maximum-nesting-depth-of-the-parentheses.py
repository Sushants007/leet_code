class Solution:
    def maxDepth(self, s: str) -> int:
        if s=="()":
            return 1
        ct=0
        count=0
        for i in range(len(s)):
            if s[i]=='(':
                count+=1
                ct=max(ct,count)                
            elif s[i]==')':
                count-=1
            

        return ct