class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        
        i = 0
        while i+1 < len(prices) and prices[i] >= prices[i+1]:
            i= i+1
        
        if i + 1 >= len(prices):
            return 0
        
        profit = 0
        for buy in range(i, len(prices)):
            for sell in range(buy+1, len(prices)):
                temp = prices[sell] - prices[buy]
                if temp > profit:
                    profit = temp
        
        return profit
                
        
        

print(Solution().maxProfit([7,6,4,3,1, 0, 0, 0 , 0, 0, 0, 0, 0 , 0, 0, 0, 0, 0 , 0, 0]))