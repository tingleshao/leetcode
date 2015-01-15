class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        k = rowIndex
        prev_row = []
        for i in xrange(k+1):
          prev_row.append(0)
        prev_row[0] = 1
        row = []
        for i in xrange(k):
          row = []
          for i in xrange(k+1):
            row.append(0)
          row[0] = 1
          for j in xrange(1,k+1):
            row[j] = prev_row[j] + prev_row[j-1]
            if row[j] == 1:
              break
          prev_row = row
        return prev_row
        
def main():
  s = Solution()
  print s.getRow(3)
     
if __name__ == "__main__":
    main()
    