class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 각 단어를 정렬하여 애너그램 구분 키로 사용
        dicOrd = {}
        for i in strs:
            sorted_str = ''.join(sorted(i))  # 단어를 정렬한 결과를 키로 사용
            if sorted_str not in dicOrd:
                dicOrd[sorted_str] = [i]
            else:
                dicOrd[sorted_str].append(i)

        print(dicOrd)
        output = list(dicOrd.values())
        print(output)

        return output