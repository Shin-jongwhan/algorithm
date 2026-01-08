class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digit = 0
        while True : 
            digits, digit_tmp = self.inc(digits, digit)
            if digit_tmp != digit : 
                digit = digit_tmp
            else : 
                break
                
        return digits
    
    def inc(self, digits, digit) : 
        n = len(digits) - digit - 1
        digits[n] += 1
        if digits[n] == 10 : 
            digits[n] = 0
            #print(digit, len(digits) - 1, digits)
            if digit == len(digits) - 1 : 
                print(digit, len(digits) - 1, digits)
                digits = [1] + digits
                return digits, digit
            else : 
                digit += 1

        return digits, digit

