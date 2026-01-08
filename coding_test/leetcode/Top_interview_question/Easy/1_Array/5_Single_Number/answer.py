class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        n = nums[0]
        blTwice = False
        output = None
        if len(nums) > 1 and nums[-1] != nums[-2] : 
            return nums[-1]
        elif len(nums) == 1 : 
            return nums[0]
        for i in range(1, len(nums)) : 
            print(nums[i], n, blTwice)
            if nums[i] == n : 
                blTwice = True
            else : 
                if blTwice == False : 
                    output = nums[i - 1]
                blTwice = False
                n = nums[i]

        return output