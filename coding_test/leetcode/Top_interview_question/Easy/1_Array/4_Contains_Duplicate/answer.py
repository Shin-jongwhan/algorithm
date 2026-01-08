class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = sorted(nums)
        #print(nums)
        output = False
        tmp = None
        for i in nums : 
            if tmp != i : 
                tmp = i
            else : 
                output = True
                
        return output