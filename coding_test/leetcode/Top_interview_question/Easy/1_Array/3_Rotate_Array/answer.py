class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 참고로 nums[:]로 써야 에러가 안 난다. 아마 버전 문제인 듯.
        totation = k % len(nums)
        nums[:] = nums[len(nums) - totation:] + nums[:len(nums) - totation]