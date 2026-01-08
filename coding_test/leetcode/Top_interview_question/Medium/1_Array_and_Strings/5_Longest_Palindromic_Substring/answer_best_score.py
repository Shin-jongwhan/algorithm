class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        
        n = len(s)
        start, size = 0, 1
        for i in range(1, n):
            l, r = i - size, i + 1
            s1, s2 = s[l-1: r], s[l: r]

            if s1 == s1[::-1] and l - 1 >= 0:
                start, size = l - 1, size + 2
            elif s2 == s2[::-1]:
                start, size = l, size + 1
        return s[start:start + size]