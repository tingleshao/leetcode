class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        res = []
        if numRows == 0:
          return []
        res.append([1])
        for i in xrange(1,numRows):
          row = [1]
          for j in xrange(1,i+1):
            if j == i:
              row.append(res[-1][j-1])
            else:
              row.append(res[-1][j]+res[-1][j-1])
          res.append(row)
        return res

def main():
    s = Solution()
    print s.generate(5)
  
if __name__ == "__main__":
    main()