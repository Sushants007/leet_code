class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap=[]
        res=[]
        if len(arr)==1:
            return arr
        for i in range(len(arr)):
            heapq.heappush(heap,(abs(arr[i]-x),arr[i]))

        while k>0:
            res.append(heapq.heappop(heap)[1])
            k-=1
        return sorted(res)   