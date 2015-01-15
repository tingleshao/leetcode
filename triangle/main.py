class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
      if len(triangle)== 0:
        return 0
      sm = 0
      for k in xrange(1, len(triangle)):
        level = triangle[k]
  #      print level
        for i in xrange(len(level)):
          if i == 0:
            level[i] += triangle[k-1][i]
          elif i == len(level)-1:
            level[i] += triangle[k-1][i-1]
          else:
            level[i] += min(triangle[k-1][i],triangle[k-1][i-1])
      return min(triangle[-1])


def main():
  
  tr = [
       [2],
      [3,4],
     [6,5,7],
    [4,1,8,3]
  ]
  s = Solution()
  print s.minimumTotal(tr)

if __name__ == "__main__":
    main()
                     
        