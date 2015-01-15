class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
       res = []
       if num == None or len(num) <=2:
           return res
       num.sort()
       for i in xrange(len(num)-1,1,-1):
         if i < len(num) -1 and num[i] == num[i+1]:
           continue
         curres = self.twoSum(num,i-1,-num[i])
         while True:
           if j < len(curres):
             curres[j].append(num[i])
           j+=1
         res.append(curres)
         
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
    S = [-1,0,1,2,-1,-4]
    print s.threeSum(S)    
  
if __name__ == "__main__":
    main()