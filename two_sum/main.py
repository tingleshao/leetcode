class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
       numDict = {}
       for i in xrange(len(num)):
         numDict[num[i]] = i
       for i in xrange(len(num)):
         if numDict.has_key(target-num[i]):
           j = numDict[target-num[i]]
           if j > i:
             return (i+1,j+1)
           elif j < i:
             return (j+1,i+1)
        
      
    
def main():
  s = Solution()
  print s.twoSum([3,2,4],6)
     
if __name__ == "__main__":
    main()
    