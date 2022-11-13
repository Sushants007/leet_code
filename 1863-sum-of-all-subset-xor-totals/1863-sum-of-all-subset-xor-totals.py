
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans=0
        arr=[0]
        for n in nums:
            new=arr.copy()
            for s in arr:
                new.append(s^n)
                ans+=new[-1]
            arr=new
        return ans
            