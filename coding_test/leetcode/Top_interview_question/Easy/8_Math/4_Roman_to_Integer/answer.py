class Solution:
    def romanToInt(self, s: str) -> int:
        dicRoman_num = {
            'I' : 1, 
            'V' : 5, 
            'X' : 10, 
            'L' : 50, 
            'C' : 100, 
            'D' : 500, 
            'M' : 1000
        }
        
        o = 0
        
        for i in range(0, len(s) - 1) : 
            if dicRoman_num[s[i]] < dicRoman_num[s[i + 1]] : 
                o -= dicRoman_num[s[i]]
            else : 
                o += dicRoman_num[s[i]]

        o += dicRoman_num[s[-1]]
        
        return o