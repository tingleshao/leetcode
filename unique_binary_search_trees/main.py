class Solution:
    # @return an integer
    def numTrees(self, n):
        ans = 1.0
        for i in xrange(1,n+1):
          ans = ans *2 * (2*i-1)/(i+1)
        return int(ans)
        
                      
def main():
    s = Solution()
    print s.numTrees(4)
    
if __name__ == "__main__":
    main()