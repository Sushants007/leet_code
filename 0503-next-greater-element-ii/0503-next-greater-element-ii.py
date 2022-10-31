class Solution:
    def nextGreaterElements(self, arr: List[int]) -> List[int]:
        stack = []
        n=len(arr)
        res = [0]*n          
        i = 2*len(arr) - 1
        while i>=0:
            if stack and arr[stack[-1]]<=arr[ i%n ]:
                stack.pop()
                continue  
            elif not stack:
                  res[i%n]=-1                  
            elif arr[stack[-1]]>arr[i%n]:
                res[i%n]=arr[stack[-1]]
           
            stack.append(i%n)
            i -= 1
        return(res) 