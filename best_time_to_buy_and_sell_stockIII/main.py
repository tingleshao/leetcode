class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
      n = len(prices)
      if n == 0:
        return 0
        
      historyProfit = [0 for i in xrange(n)]
      futureProfit = [0 for i in xrange(n)]
      
      valley = prices[0]
      peak = prices[n-1]
      maxP = 0
      
      for i in xrange(n):
        valley = min(valley, prices[i])
        if i > 0:
          historyProfit[i] = max(historyProfit[i-1],prices[i]-valley)
          
      for i in xrange(1,n+1):
        peak = max(peak, prices[-i])
        if i > 1:
          futureProfit[-i] = max(futureProfit[-(i-1)], peak-prices[-i])
        maxP = max(maxP, historyProfit[-1]+futureProfit[-i])
      return maxP

def main():
  s = Solution()
  print s.maxProfit([1,2,3,4,5])
if __name__ == "__main__":
    main()
             