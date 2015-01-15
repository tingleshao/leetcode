class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
      if num == []:
        return None
      if len(num)==1:
        return num[0]
      for i in xrange(1,len(num)-1):
        if num[i] > num[i]+1:
          return num[i]+1
      return num[0]
        
  
          
            
def main():
  s = Solution()
  print s.findMin()
  
if __name__ == "__main__":
    main()