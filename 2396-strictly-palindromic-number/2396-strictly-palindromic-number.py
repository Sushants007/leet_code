class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2,n-1):
            rep = []
            k = n
            while k > 0:
                rep.append(k%i)
                k //= i
            if rep != rep[::-1]: return False
        return True