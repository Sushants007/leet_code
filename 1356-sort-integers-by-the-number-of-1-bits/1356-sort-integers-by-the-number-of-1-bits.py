class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key = lambda x: (self.countOnes(x), x))        
    def countOnes(self, x: int) -> int:
        count = 0
        while x:
            x &= (x - 1)
            count += 1
        return count
