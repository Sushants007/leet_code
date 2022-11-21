class Solution:
    def commonChars(self, A: List[str]) -> List[str]:

        if len(A)<2 : 
            return A
        alist = set(A[0])
        res = []
        for one in alist:
            
            n = min([a_word.count(one) for a_word in A])    
            if n:    
                res += [one]*n
        return res