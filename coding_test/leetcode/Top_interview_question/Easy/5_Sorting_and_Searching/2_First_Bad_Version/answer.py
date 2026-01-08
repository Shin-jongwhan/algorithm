# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        high = n
        mid = (high + low) // 2
        if (n > 1 and isBadVersion(high) == True and isBadVersion(high - 1) == False) : 
            return high
        elif isBadVersion(1) == True : 
            return 1

        while True : 
            print(mid, isBadVersion(mid))
            if isBadVersion(mid) == True : 
                if isBadVersion(mid - 1) == False : 
                    return mid
                high = mid
                mid = (high + low) // 2
            else : 
                if isBadVersion(mid + 1) == True : 
                    return mid + 1
                low = mid
                mid = (high + low) // 2
