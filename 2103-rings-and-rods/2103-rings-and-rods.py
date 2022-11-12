class Solution:
    def countPoints(self, rings: str) -> int:
        c=0
        arr=['']*10
        for i in range(1,len(rings),2):
            arr[int(rings[i])]+=rings[i-1]
        for j in arr:
            if 'R' in j and "G"in j and "B" in j:
                c+=1
        return c