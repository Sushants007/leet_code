class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        arr = []
        for i in sentences:
            a = i.split(" ")
            arr.append(len(a))
        return max(arr)
