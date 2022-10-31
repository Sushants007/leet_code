class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        res = []
        for i in range(0,n-1):
            j = i+1
            while j<n-1 and prices[j]>prices[i]:
                j+=1            
            if j==n-1 and prices[j]>prices[i]:
                res.append(prices[i])
            else:
                res.append(prices[i]-prices[j])
        return res + [prices[n-1]]
