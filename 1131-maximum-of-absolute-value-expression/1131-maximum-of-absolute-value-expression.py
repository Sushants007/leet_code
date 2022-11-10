class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
	
        l1, l2, l3, l4 = [] , [], [], []
        for i in range(len(arr1)):
            l1.append(i + arr1[i] + arr2[i])
            l2.append(i - arr1[i] + arr2[i])
            l3.append(i - arr1[i] - arr2[i])
            l4.append(i + arr1[i] - arr2[i])
            
        max_absolute_difference = 0
        max_absolute_difference = max(max_absolute_difference, max(l1) - min(l1))
        max_absolute_difference= max(max_absolute_difference, max(l2) - min(l2))
        max_absolute_difference= max(max_absolute_difference, max(l3) - min(l3))
        max_absolute_difference= max(max_absolute_difference, max(l4) - min(l4))
        
        
        return max_absolute_difference