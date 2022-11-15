class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ct=0
        for i in range(len(arr)):
            acc=arr[i]
            for k in range(i+1,len(arr)):
                acc^=arr[k]
                if acc==0:
                    ct+=k-i
        return ct