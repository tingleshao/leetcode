class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
      n1 = int(num1)
      n2 = [int(i) for i in num2]
      res = 0
      for i in xrange(len(n2)):
        res+= n1*n2[i]
        res *=10
        print i, n1, n1*n2[i]
      res /= 10
      return str(res)
                              
def main():
    s = Solution()
    print s.multiply("123","456")
    
if __name__ == "__main__":
    main()