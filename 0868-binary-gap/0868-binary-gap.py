class Solution:
    def binaryGap(self, n: int) -> int:
        pre=0
        dist=0
        for i ,c in enumerate(bin(n)[2:]):
            if c=='1':
                dist =max(dist, i-pre)
                pre=i
        return dist