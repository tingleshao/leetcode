class Solution:
    # @return a string
    def getPermutation(self, n, k):
        code = [0 for j in xrange(n)]
        k = k-1
        i = n-1
        div = 0
        i = 0
        while i < k:
          for j in xrange(0,n):
            sm = code[-(j+1)] + 1
            if sm > j:
              code[-(j+1)] = 0
            else:
              code[-(j+1)] = sm
              break
          i+=1
        res = ""
        lsts = [j for j in xrange(1,n+1)]
        for i in code:
            res = res + str(lsts[i])
            lsts.pop(i)
        return res
        



def main():
  s = Solution()
  n = 3
  k = 3
  print s.getPermutation(n,k)
  print s.getPermutation(9,273815)
  
  
  
if __name__ == "__main__":
    main()
             