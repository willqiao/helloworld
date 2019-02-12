test = [7,1,5,3,6,4]

    
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        index = 0
        for i in range(prices.__len__()):
            if (prices[i] > prices[index]):
                


