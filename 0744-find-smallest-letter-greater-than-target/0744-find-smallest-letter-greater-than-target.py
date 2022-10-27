class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        st=0
        end=len(letters)
        result=0
        if target >= letters[-1] or target < letters[0]:
            return letters[0]
        while st<=end:
            mid= st+(end-st)//2
            if letters[mid]==target:
                st=mid+1
            elif letters[mid]<target:
                st= mid+1
            elif letters[mid]>target:
                result = letters[mid]
                end=mid-1
            #elif target not in letters:
             #   result = letter[0]
        return result