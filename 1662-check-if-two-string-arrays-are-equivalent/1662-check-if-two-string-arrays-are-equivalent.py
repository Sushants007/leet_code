class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        a=''
        b=''
        for i in range(len(word1)):
            a=a+word1[i]
        for i in range(len(word2)):
            b=b+word2[i]
        if a==b:
            return True