class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        max_profit = 0
        if not prices:
        	return max_profit
        else:
        	min_element = prices[0]
        for i in range(0, len(prices)):
        	if prices[i] < min_element:
        		min_element = prices[i]
        	if (prices[i] - min_element) > max_profit:
        		max_profit =  prices[i] - min_element
        return max_profit

S = Solution()
nums = []
out = S.maxProfit(nums)
print(out)