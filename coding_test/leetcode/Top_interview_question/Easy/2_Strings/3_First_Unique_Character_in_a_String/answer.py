class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 등장순서
        # 각 문자의 등장 개수
        ## * 참고로 딕셔너리는 순서가 없긴 하지만 여기서는 무시한다.
        dicOrder = {}
        dicNum_chr = {}

        n = 1
        for i in range(0, len(s)) : 
            if s[i] not in dicNum_chr.keys() : 
                dicNum_chr[s[i]] = [i]
                dicOrder[n] = s[i]
                n += 1
            else : 
                dicNum_chr[s[i]].append(i)

        print(dicNum_chr)
        print(dicOrder)
        for i in dicOrder.keys() : 
            if len(dicNum_chr[dicOrder[i]]) == 1 : 
                #print(dicNum_chr[dicOrder[i]][0])
                return dicNum_chr[dicOrder[i]][0]

        return -1