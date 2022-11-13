class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a=min(nums)
        b=max(nums)
        arr=[]
        for i in range(1,a+1):
            if a%i==0 and b%i==0:
                arr.append(i)
        return max(arr)
               