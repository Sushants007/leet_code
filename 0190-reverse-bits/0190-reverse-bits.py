class Solution:
    def reverseBits(self, n: int) -> int:
        bit_str = '{:032b}'.format(n)
        reverse=bit_str[::-1]
        return int(reverse,base=2)