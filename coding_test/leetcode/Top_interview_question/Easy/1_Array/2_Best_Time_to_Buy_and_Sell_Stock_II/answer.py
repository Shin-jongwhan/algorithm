class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        nOutput = 0
        buy = prices[0]
        for i in range(0, len(prices)) : 
            if prices[i] - buy > 0 : 
                nOutput += prices[i] - buy
                buy = prices[i]
            else : 
                buy = min(buy, prices[i])

        #print(nOutput)
        return nOutput