class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[0]*(n+1)
        ofset=1
        for i in range(1,n+1):
            if ofset*2==i:
                ofset=i
            ans[i]=1+ans[i-ofset]
        return ans