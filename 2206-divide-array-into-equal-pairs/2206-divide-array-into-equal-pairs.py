class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums)//2<len(set(nums)):
            return False
        for i in range(len(nums)):
            if nums.count(i)%2==1:
                return False
        return True
