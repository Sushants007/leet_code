class Solution:
    def minWindow(self, s: str, t: str) -> str:
        map=collections.Counter(t)
            
        i=0
        j=0
        l=0
        r=0
        count=len(t)        
        
        while r<len(s) :
            if map[s[r]]>0:
                count-=1
            map[s[r]]-=1
            r+=1
            while count == 0:
                if j==0 or r-l < j-i:
                    i,j=l,r
                map[s[l]]+=1
                if map[s[l]]>0:
                    count +=1
                l += 1
        return s[i:j]
                    
            