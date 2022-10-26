class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        for i in range (len(nums)):
            if i!=0 and i!=len(nums)-1:
                if(nums[i]!=nums[i+1] and nums[i]!=nums[i-1]):
                    return nums[i]
            if(i==0 and nums[i]!=nums[i+1]):
                return nums[i]
            if(i==len(nums)-1 and nums[i]!=nums[i-1]):
                return nums[i]
        return -1            