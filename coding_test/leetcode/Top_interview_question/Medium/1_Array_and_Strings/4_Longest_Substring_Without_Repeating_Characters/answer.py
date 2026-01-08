class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dicChar = {}
        o = 0
        start = 0
        length= 0
        for i in range(0, len(s)) : 
            if s[i] in dicChar and dicChar[s[i]] >= start :
                start = dicChar[s[i]] + 1
                dicChar[s[i]] = i
            else : 
                dicChar[s[i]] = i
                length = i - start + 1
                if o < length : 
                    o = length
            

        print(o)
        return o