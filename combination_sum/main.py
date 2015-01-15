class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        pool = list(set(candidates))
        pool.sort()
        start = 0
        end = len(pool) - 1
        ll = []
        ans = []
        self.comb(target,start,end,ll,ans,pool)
        return ans 
        
    def comb(self,target,start,end,ll,ans,pool):
      if target < 0:
        return 
      if target == 0:
        ans.append(ll)
        return 
      else: 
        for i in range(start,end+1):
          lst = ll[:]
          lst.append(pool[i])
          self.comb(target-pool[i],i,end,lst,ans,pool)
      
        

def main():
  s = Solution()
  can = [2,3,6,7]
  print s.combinationSum(can,7)



if __name__ == "__main__":
    main()
                