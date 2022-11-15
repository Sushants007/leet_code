class Solution:
    def countPrimeSetBits(self, l: int, r: int) -> int:
        count=0
        for i in range(l,r+1):
            c=0
            n=bin(i).count("1")
            if n in [2, 3, 5, 7, 11, 13, 17, 19]:     
                count += 1
        return count