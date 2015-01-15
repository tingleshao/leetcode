class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) == 0:
          return 0
        min = 0
        max = prices[0]
        profit = 0
        for i in xrange(1,len(prices)):
          curr_profit = prices[i]-prices[min]
          if curr_profit > profit:
            profit = curr_profit
          elif prices[i] < prices[min]:
            min = i  
        return profit
				
    
def main():
  s = Solution()
  print s.maxProfit([1,1,2,0,1,5,1])
     
if __name__ == "__main__":
    main()
    