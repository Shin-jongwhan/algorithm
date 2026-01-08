class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        price_min = 10000 # 최저 주식값
        profit = 0 # 수익
        
        for price_current in prices:
            price_min = min(price_current, price_min)
            profit = max(profit, price_current-price_min) 
        return profit