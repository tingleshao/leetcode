class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
      result = []
      output = []
      self.DFS(s,0,output,result)
      return result
              
    def isPalindrome(self,s,start,end):
   #   print start
   #   print end
      while start < end:
        if s[start] != s[end]:
          return False
        start += 1
        end -= 1
      return True
    
    def DFS(self, s, start, output, result):
      if start == len(s):
        result.append(output)
        return
      for i in xrange(start,len(s)):
        if self.isPalindrome(s, start, i):
          output.append(s[start:i+1])
   #       print output
          self.DFS(s,i+1,list(output),result)
          output.pop(-1)
        
def main():  
    s = Solution()
    sti = "aab"
    print s.partition(sti)

if __name__ == "__main__":
    main()