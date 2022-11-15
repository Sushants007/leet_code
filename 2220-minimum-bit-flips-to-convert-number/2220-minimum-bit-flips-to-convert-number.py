class Solution:
    def minBitFlips(self, x: int, y: int) -> int:
        Xor, ans = x ^ y, 0
        while Xor:
            ans += Xor & 1
            Xor >>= 1
        return ans        