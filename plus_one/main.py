class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        curr = len(digits) - 1 
        curry = 0
        while True:
          if digits[curr] == 9:
            digits[curr] = 0
            curr -= 1
            curry = 1
          else:
            digits[curr] += 1
            curry = 0
            return digits
          if curr == -1:
            if curry == 1:
              digits.insert(0,1)
            return digits
        
    
def main():
  s = Solution()
  print s.plusOne([3])
     
if __name__ == "__main__":
    main()
    