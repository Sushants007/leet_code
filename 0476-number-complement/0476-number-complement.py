class Solution:
    def findComplement(self, num: int) -> int:
        output = ''
        for i in bin(num)[2:]:
            if i == '0':
                output += '1' 
            else:
                output += '0' 

        return int(output,2)