class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        prev_words=0
        for i in range(len(s)):
            
            if s[i] == ' ':
                if i!= 0 and s[i-1] != ' ':
                    prev_words += 1
            if prev_words == k:
                return(s[0:i])
        return(s)