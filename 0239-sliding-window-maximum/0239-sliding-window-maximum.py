class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_vals = []
        ans = []
        i = j = 0
        n = len(nums)
        while(j<n):
            if len(max_vals)==0:
                max_vals.append(nums[j])
            else:
                while len(max_vals)!=0 and max_vals[-1]<nums[j]:
                    max_vals.pop(-1)
                max_vals.append(nums[j])
            # print(max_vals, end=' ')
            if (j-i+1)<k:
                j = j+1
            elif (j-i+1):
                ans.append(max_vals[0])
                if nums[i]==max_vals[0]:
                    max_vals.pop(0)
                i = i+1
                j = j+1
            # print(max_vals)
        return ans