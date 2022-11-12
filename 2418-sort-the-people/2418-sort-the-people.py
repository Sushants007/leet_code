class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ln=len(heights)
        mp={}
        for i in range(len(heights)):
            mp[heights[i]]=names[i]
        heights.sort(reverse=True)
        res=[]
        for j in range(len(heights)):
            res.append(mp[heights[j]])
        return res