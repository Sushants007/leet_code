class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() 
        ans=[]
        for i in range(len(nums)):
            while len(q)!=0 and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
   
            if len(q)!=0 and q[0] == i - k:
                q.remove(q[0])

            if i >= k - 1:
                ans.append(nums[q[0]])
        return ans        
        
