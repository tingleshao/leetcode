class Solution:
    # @return a string
    def countAndSay(self, n):
      prev = "1"
      if n == 0:
        return prev
      i = 1
      while i < n:
        curr = ""
        p = 0
        c = p
        cp = prev[p]
        count = 0
        while c < len(prev):
          cc = prev[c]
          if cc == cp:
            count += 1
          else:
            curr = curr + str(count)
            curr += cp
            count = 1
            p = c
            cp = prev[p]
          c += 1
        curr += str(count)
        curr += cc
        prev = curr
    #    print "curr: " + curr
        i+=1
      return prev
        
        
		
		
def main():
  s = Solution()
  print s.countAndSay(4)
  

     
if __name__ == "__main__":
    main()
           