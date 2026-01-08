class Solution(object):
    def fibonacci_sequence(self, n):
        prev = 0
        out = 1
        for i in range(0, n) : 
            tmp = out
            out += prev
            prev = tmp

        return out
    
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.fibonacci_sequence(n)