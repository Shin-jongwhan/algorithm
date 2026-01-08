class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output = [0, 0]
        blOutput = False
        for i in range(0, len(nums) - 1) : 
            for j in range(i + 1, len(nums)) : 
                if nums[i] + nums[j] == target : 
                    output = [i, j]
                    blOutput = True
                    break
            if blOutput == True : 
                break
                
        return output