import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0 : 
            return False
        o = math.log(abs(n), 3)
        tolerance = 1e-14  # 허용 오차 설정
        
        #return abs(o - round(o)) < tolerance
        return math.isclose(o, round(o), rel_tol=1e-15)