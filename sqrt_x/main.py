class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
       left = 1
       right = x
       ans = x
       while left <= right:
         mid = left + (right-left) /2 
         if mid <= (x / mid):
           left = mid + 1
           ans = mid 
         else:
           right = mid - 1
        
       return ans
        

def main():
  s = Solution()

  print s.sqrt(3)
  print s.sqrt(4)
  
  
  
  

if __name__ == "__main__":
    main()
             