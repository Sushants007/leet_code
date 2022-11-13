class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        #if highLimit<10 and highLimit!=lowLimit:
        #    return 1
        cnt, mx = [0] * 46, 0
        for i in range(lowLimit, highLimit + 1):
            sm = 0
            while i > 0:
                sm += i % 10
                i //= 10
            cnt[sm] += 1
            mx = max(mx, cnt[sm])
        return mx
