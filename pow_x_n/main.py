class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n == 0:
          return 1
        if n < 0:
          m = (-n/2)*-1
        temp = self.pow(x,m)
        if n%2 == 0:
          return temp * temp
        else:
          if n > 0:
            return temp * temp * x
          else:
            return temp * temp / x
        
          
def main():
    s = Solution()
    print s.pow(	34.00515, -3)
    
    
if __name__ == "__main__":
    main()