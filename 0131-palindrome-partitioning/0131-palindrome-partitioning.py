class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        t=[[-1*(len(s)+1)]*(len(s)+1)]
        self.helper(res, [], s)
        return res

        
    def helper(self, res, curr, s):
        if s == "":
            res.append(curr)

        for i in range(len(s)):
            if self.isPalindrome(s[:i + 1]):  
                self.helper(res, curr + [s[:i + 1]], s[i + 1:])
    def isPalindrome(self, s):
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True