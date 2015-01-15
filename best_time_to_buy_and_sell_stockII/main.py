class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        res  = 0
				for i in xrange(len(prices)-1):
						if prices[i] < prices[i+1]:
							res += prices[i+1] - prices[i]
				return res
				
				