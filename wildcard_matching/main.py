class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
      if p == "":
          return s == ""
      if s == "":
          return p == "*"
      star = ""
      ss = s[0]
  #    print "6"
      while s != "":
        if len(p) > 0 and ( p[0] == "?" or p[0] == s[0] ):
          p = p[1:]
          s = s[1:]
   #       print "1"
          
          continue
        if len(p) > 0 and  p[0] == "*":
          star = p
          p = p[1:]
          ss = s
   #       print "2"
          
          continue
          
        if star != "" and len(star) > 0:
          p = star[1:]
          s = ss
          ss = ss[1:]
    #      print "3"
          
          continue
     #   print "5"
        return False
      while len(p) > 0 and p[0] == "*":
        p = p[1:]
     #   print "4"
      return not(p != "")
                              
def main():
    s = Solution()
    print s.isMatch("aa","a") # f
    print s.isMatch("aa","aa")# t
    print s.isMatch("aaa","aa")#f 
    print s.isMatch("aaa","*") #t
    print s.isMatch("aaa","a*")#t
    print s.isMatch("ab","?*") #t
    print s.isMatch("aab","c*a*b")#f
    print s.isMatch("aaabababaaabaababbbaaaabbbbbbabbbbabbbabbaabbababab", "*ab***ba**b*b*aaab*b" #t
)
    
    
if __name__ == "__main__":
    main()