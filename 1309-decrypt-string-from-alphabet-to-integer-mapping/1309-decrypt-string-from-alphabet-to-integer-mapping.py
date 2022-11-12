class Solution:
    def freqAlphabets(self, s: str) -> str:
        i=len(s)-1
        ans=[]
        while i>=0:
            if s[i]=='#':
                ans.append(self.alpha(s[i-2:i]))
                i-=3
            else:
                ans.append(self.alpha(s[i]))
                i-=1
        return ''.join(reversed(ans))
    def alpha(self,num):
        return chr(int(num)+ord('a')-1)
            