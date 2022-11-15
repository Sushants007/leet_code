class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c=0
        for mins in s:
            c^=ord(mins)
        for mint in t:
            c^=ord(mint)
        return chr(c)