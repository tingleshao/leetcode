class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        num.sort()
        max_len = 1
        curr_len = 1
        for i in xrange(len(num)-1):
          if num[i+1] - num[i] == 1 or num[i+1] - num[i] == 0 :
            if num[i+1] - num[i] == 1:
              curr_len += 1
          else:
            if curr_len > max_len:
              max_len = curr_len
              
            curr_len = 1
        if curr_len > max_len:
          max_len = curr_len
        
        return max_len
				
				
          
    
def main():
  s = Solution()
  num  = [100, 4, 200, 1, 3, 2]
  num2  = [0,-1]
  num3 = [1,2,0,1]  
  print s.longestConsecutive(num)

  print s.longestConsecutive(num2)
  
  print s.longestConsecutive(num3)

     
if __name__ == "__main__":
    main()