class Solution:
    def toHex(self, num: int) -> str:
        if not num:
            return "0"
        mp='0123456789abcdef'
        res=''
        for i in range (8):
            n=num&15
            c=mp[n]
            res=c+res
            num=num//16
            if num==0:
                break
        return res