class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans=[]
        isdivi=True
        for i in range(left,right+1):
            if i<10:
                ans.append(i)
            elif '0' not in str(i):
                for d in str(i):
                    if i%int(d):
                        isdivi=False
                        break
                if isdivi:
                    ans.append(i)
                isdivi= True
        return ans