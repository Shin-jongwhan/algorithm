class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        opt = [0] * n
        opt[0], opt[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            opt[i] = max(nums[i] + opt[i-2], opt[i-1])

        return opt[n-1]