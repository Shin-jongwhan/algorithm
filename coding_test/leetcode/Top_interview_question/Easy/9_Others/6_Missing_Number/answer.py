class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        st = set(range(0, len(nums) + 1))
        for i in nums : 
            st.remove(i)

        return st.pop()