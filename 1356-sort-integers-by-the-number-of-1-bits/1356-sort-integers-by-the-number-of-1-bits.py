class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        res=[]
        for num in arr:
            ones=self.count(num)
            res.append((ones,num))
        heapq.heapify(res)
        finalres=[]
        while len(res)>0:
            finalres.append(heappop(res)[1])
        return finalres
    def count(self,n):
        ct=0
        while n:
            n&=n-1
            ct+=1
            n//=2
        return ct