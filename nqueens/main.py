class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        result = []
        cfr = [0 for i in xrange(n)]
        self.helper(n,0,cfr,result)
        return result
        
    def helper(self,n,row,colForRows,result):
      if n == row:
        ress = []
  #      print colForRows
        for i in xrange(n):
          res = ""
          for j in xrange(n):
            if colForRows[i] == j:
              res = res + "Q"
            else:
              res = res + "."
          ress.append(res)
        result.append(ress)
        return
      else:
        for i in xrange(n):
          cfr = list(colForRows)
          cfr[row] = i  
          if self.check(row,cfr):
            self.helper(n,row+1,cfr,result)
    
    def check(self,row,colForRows):
      for i in xrange(row):
        if colForRows[row] == colForRows[i] or abs(colForRows[row] - colForRows[i]) == row-i:
          return False
      return True
      
          

def main():  
    s = Solution()
    print s.solveNQueens(4)
    


if __name__ == "__main__":
    main()