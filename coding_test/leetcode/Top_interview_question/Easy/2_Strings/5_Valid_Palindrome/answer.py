class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = "".join([i for i in s.lower() if (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 48 and ord(i) <= 57)])
        if len(s) % 2 == 1 : 
            if s[:int(len(s) / 2) : -1] == s[ : int(len(s) / 2)] : 
                return True
            else : 
                return False
        else : 
            if s[:int(len(s) / 2) - 1 : -1] == s[ : int(len(s) / 2)]  : 
                return True
            else : 
                return False