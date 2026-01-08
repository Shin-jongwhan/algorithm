class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0 : 
            output = int(str(x)[::-1])
        else : 
            output = int("-" + str(x)[:0:-1])
        
        if output < -2**31 or output > 2**31 - 1 : 
            return 0
        
        return output