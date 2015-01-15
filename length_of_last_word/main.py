class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        if s == "":
          return 0
        start = 1
        end = 1
        lens = len(s)
        c = s[-end]
        while c == " ":
          end += 1
          start += 1
          if end > lens:
            return 0
          c = s[-end]
        while c != " ":
          end += 1
          if end > lens:
            return end - start
          c = s[-end]
        return end - start
        
          

          
				

def main():
  s = Solution()
  w = "Hello World"
  a = "a"
  b = "  "
  aa = " a "
  n = s.lengthOfLastWord(w)
  print n
  
if __name__ == "__main__":
    main()