class Solution:
    def trap(self, height: List[int]) -> int:
        mxl=[0]*(len(height))
        mxr=[0]*(len(height))
        water=[0]*(len(height))
        sum=0
        mxl[0]=height[0]
        mxr[len(height)-1]=height[len(height)-1]
        for i in range(0,len(height),1):
            mxl[i]=max(mxl[i-1],height[i])
        for i in range(len(height)-2,0,-1):
            mxr[i]=max(mxr[i+1],height[i])
        for i in range (1,len(height),1):
            sum+= min(mxl[i],mxr[i])-height[i]
        
        return sum    
        