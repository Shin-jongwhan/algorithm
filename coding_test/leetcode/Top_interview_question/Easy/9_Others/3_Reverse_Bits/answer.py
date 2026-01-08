class Solution:
    def reverseBits(self, n: int) -> int:
        return int("{0:0>32}".format(bin(n)[2:])[::-1], 2)