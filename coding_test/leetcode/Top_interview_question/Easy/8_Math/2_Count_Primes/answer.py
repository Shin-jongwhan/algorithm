class Solution(object):
    def sieve_of_eratosthenes(self, limit):
        if limit in [0, 1] : 
            return [limit]
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False  # 0과 1은 소수가 아님

        for i in range(2, int(limit ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, limit + 1, i):
                    sieve[j] = False

        return [num for num, is_prime in enumerate(sieve) if is_prime]
    
    
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        output = self.sieve_of_eratosthenes(n)
        if output[-1] == n : 
            del output[-1]
        return len(output)