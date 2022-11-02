class Solution:
    def kClosest(self, p: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        res=[]
        for i in range(0,len(p),1):
            dist=(p[i][0]*p[i][0])+(p[i][1]*p[i][1])
            heapq.heappush(heap,(dist,(p[i][0],p[i][1])))         
            
        
        count=0
        while count<k:
            res.append(heapq.heappop(heap)[1])
            count+=1
        return res