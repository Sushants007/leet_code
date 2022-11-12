class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = 0
        ans = []
        
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                ans.append(alpha(s[i:i+2]))
                i += 3
            else:
                ans.append(alpha(s[i]))
                i += 1
        
        return ''.join(ans)
                

def alpha(num):
    return chr(int(num) + ord('a') - 1)