class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, -1, -1) : 
            if nums[i] == 0 : 
                if i != 0 : 
                    nums[:] = nums[:i] + nums[i+1:] + [0]
                else : 
                    nums[:] = nums[1:] + [0]