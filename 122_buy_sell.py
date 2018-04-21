class Solution(object):
    def maxProfit(self, prices):

        sum=0
        for i in range(0,len(prices)-1):
            if prices[i+1]>prices[i]:
                sum = sum+prices[i+1]-prices[i]
        return sum

S = Solution()
s = [1,2,3,6]
out = S.maxProfit(s)
print(out)