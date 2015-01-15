
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        num.sort()
        res = []
        res.append(list(num))
        n = len(num) 
        while True:
          
          i = n - 1 
          while i > 0:
            if num[i-1] < num[i]:
              break
            i-=1
          if i == 0:
            break
          j = n-1
          while j > i-1:
            if num[j] > num[i-1]:
              break
            j-=1
            
          self.swap(num,i-1,j)
          self.rev(num,i,n-1)
          res.append(list(num))
        return res
    
    def swap(self,a,i,j):
      temp = a[i]
      a[i] = a[j]
      a[j] = temp
      
    def rev(self,a,i,j):
      while i<j:
        self.swap(a,i,j)
        i+=1
        j-=1
      return
          
        
                            
def main():
  s = Solution()
  print s.permuteUnique([1,1,2])

if __name__ == "__main__":
    main()