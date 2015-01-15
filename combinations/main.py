class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
     res = []
     l = []
     self.comb(n,k,1,res,l)
     return res
     
     
    def comb(self,n,k,start,result,l):
      if k == 0:
        result.append(l)
      else:
        for i in xrange(start,n+1):
          a = list(l)
          a.append(i)
          self.comb(n,k-1,i+1,result,a)
        
        
				
    
def main():
  s = Solution()
  print s.combine(4,2)
     
if __name__ == "__main__":
    main()
    