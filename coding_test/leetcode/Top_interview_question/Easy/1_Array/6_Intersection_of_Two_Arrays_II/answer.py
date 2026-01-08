from collections import Counter


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 1. 각 숫자가 몇 번 등장하는지 센다. 딕셔너리 형태로 key : 중복 횟수
        # 2. 교집합을 구한다.
        # 3. 교집합을 구한 다음 딕셔너리에서 중복 횟수를 찾아서 리턴한다.
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)

        return list((counter1 & counter2).elements())