class Solution:
    def commonChars(self, A: List[str]) -> List[str]:

        alphabet = string.ascii_lowercase
        d = {c:len(A)  for c in alphabet}
        
        for k, v in d.items():
            for word in A:
                d[k] = min(d[k],word.count(k))

        res = []
        for c, n in d.items():
            if n > 0:
                res += [c] * n
        return res