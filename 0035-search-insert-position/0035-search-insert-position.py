class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)-1
        while lo <= hi:
            if (lo+hi)%2 == 0: mid = (lo+hi)//2
            else: mid = (lo+hi-1)//2

            if nums[mid] == target: return mid
            elif nums[mid] < target:
                if lo == hi: return mid+1
                lo = mid+1
            else:
                if lo == hi: return mid
                hi = mid