class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        purchased = False
        buyday = 0
        for index in range(prices.__len__()):
            if index == prices.__len__() -1:
                if purchased:
                    profit += prices[index] - prices[buyday]
                    continue
                else:
                    continue
            
            if prices[index] < prices[index + 1]:
                if (purchased == False) : 
                    buyday = index
                    purchased = True
                continue
            if prices[index] > prices[index+1]:
                if (purchased == True):
                    profit += prices[index] - prices[buyday]
                    purchased = False
                    
        return profit


        
print(Solution().maxProfit([7,1,5,3,6,4]))