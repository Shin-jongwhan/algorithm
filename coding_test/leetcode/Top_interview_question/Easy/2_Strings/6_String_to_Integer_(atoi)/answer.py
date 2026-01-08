class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()
        s2 = ""

        blZero_ignore = False
        for i in range(0, len(s)) : 
            #print(i, s[i])
            if i == 0 : 
                if s[i] == "-" or s[i] == "+" or s[i].isnumeric() == True and s[i] != '0' : 
                    s2 += s[i]
                    blZero_ignore = True
                elif s[i].isnumeric() == False : 
                    return 0
            else : 
                if s[i].isnumeric() == True : 
                    if blZero_ignore == False and s[i] == '0' : 
                        continue
                    else : 
                        s2 += s[i]
                        blZero_ignore = True
                elif s[i].isnumeric() == False : 
                    break

        if len(s2) == 0: 
            return 0
        elif s2 == '-' or s2 == '+': 
            return 0

        s2 = int(s2)
        if s2 < -(2 ** 31) : 
            return -2 ** 31
        elif s2 > 2 ** 31 - 1 : 
            return 2 ** 31 - 1
        else : 
            return s2