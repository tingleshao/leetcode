class Solution:
    # @return a boolean
    def isPalindrome(self, x):
      lens = 1

      if x < 0:
        return False
      while x % (10**lens) != x:
        lens += 1
      if lens == 1:
        return True
      uppers = 0 
      lowers = 0
      t = x
      y = x
      while x != 0:
        if x % 10 != x / (10**(lens-1)):
          return False
        x = x - (x / (10**(lens-1))) * (10**(lens-1))
        x = x / 10
        lens = lens -2
        #print x
      return True
				
    
def main():
  s = Solution()
  print s.isPalindrome(2147483647)
     
if __name__ == "__main__":
    main()
    