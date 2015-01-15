



class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
      start = 0
      tank = 0
      total = 0
      for i in xrange(len(gas)):
        tank = tank + gas[i] - cost[i]
        if tank < 0:
          start = i+ 1
          total += tank
          tank = 0
      if total + tank < 0:
          return -1
      return start
          
        
        
            
def main():
  s = Solution()
  print s.addBinary("11","1")

if __name__ == "__main__":
    main()