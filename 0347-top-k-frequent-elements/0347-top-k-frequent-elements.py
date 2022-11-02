class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map={}
        res=[]
        for hash in nums:
            if hash in map:
                map[hash]+=1
            else:
                map[hash]=1
        heap=[]
        for key in map:
            heapq.heappush(heap,(-map[key],key))
        while k>0:
            res.append(heapq.heappop(heap)[1])
            k-=1
        return res