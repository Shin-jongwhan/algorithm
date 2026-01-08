class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1 : 
            return s
        elif len(s) == 2 :
            if s[0] == s[1] : 
                return s
            else : 
                return s[0]

        o = ""
        pt = ""		# palindrome tmp
        for i in range(1, len(s)) : 
            if s[i] == s[i - 2] : 		# odd
                pt = s[i - 2 : i + 1]
                n = 1
                while ((i - 2 - n) >= 0 and (i + n) <= len(s) - 1) and s[i - 2 - n] == s[i + n] : 
                    pt = s[i - 2 - n : i + n + 1]
                    n += 1
                if len(o) < len(pt) : 
                    o = pt
            if s[i] == s[i - 1] : 		# even
                pt = s[i - 1 : i + 1]
                n = 1
                while ((i - 1 - n) >= 0 and (i + n) <= len(s) - 1) and s[i - 1 - n] == s[i + n] : 
                    pt = s[i - 1 - n : i + n + 1]
                    n += 1
                if len(o) < len(pt) : 
                    o = pt

        if o == "" : 
            return s[0]
        else : 
            return o