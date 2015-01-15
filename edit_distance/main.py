class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
      table = [[0 for j in xrange(len(word2)+1)] for i in xrange(len(word1)+1)]
      for i in xrange(len(word1)+1):
        table[i][0] = i
      for j in xrange(len(word2)+1):
        table[0][j] = j
      for i in xrange(1,len(word1)+1):
        for j in xrange(1,len(word2)+1):
          if word1[i-1] != word2[j-1]:
            e = 1
          else: 
            e = 0
          table[i][j] = min([table[i-1][j]+1,table[i][j-1]+1,table[i-1][j-1]+e])
      return table[-1][-1]
                 
def main():  
    s = Solution()

   
if __name__ == "__main__":
    main()