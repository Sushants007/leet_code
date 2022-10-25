class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
          mid = (left + right)//2
          if left == right:
            return nums[left]
          elif nums[mid] > nums[right]:
            left = mid + 1
          else:
            right = mid
        