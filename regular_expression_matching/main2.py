class Solution:
    # @return a boolean
    def isMatch(self,s, p):
      #print "heres: " + s + "and " + str((s!= "") )
      if p == "":
        return  s == ""
      
      if (len(p) > 1 and p[1] != "*") or (len(p) == 1):
        if s == "" or (not self.matchFirst(s[0],p[0])):
          return False
        return self.isMatch(s[1:],p[1:])
      else:
   #     print p,s
        if len(p) >= 2 and self.isMatch(s,p[2:]):
          return True
        while len(p) > 0 and len(s) > 0 and (self.matchFirst(s[0],p[0])):
          s = s[1:]
          if (len(p) >= 2 and self.isMatch(s,p[2:])) or (len(p) == len(s) == 0) :
            return True
        return s == p == ""
  
    def matchFirst(self,s,p):
      return p == s or (p == "." and s!= '')
    
              			
def main():
    
    s = Solution()
    print s.isMatch("aa","a") 
    print "---2---"
    print s.isMatch("aa","aa") 
    print "---3---"  
    print s.isMatch("aaa","aa") 
    print "---4---"
    print s.isMatch("aa", "a*") 
    print "---5---"
    print s.isMatch("aa", ".*") 
    print "---6---"
    print s.isMatch("ab", ".*") 
    print "---7---"
    print s.isMatch("ab", "a*b")
    print "---8---"
    print s.isMatch("aaa", "ab*a*c*a")
    print "---9---"
    print s.isMatch("ab",".*c")
    print "---10---"
    print s.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")
    print s.isMatch("baccbbcbcacacbbc", "c*.*b*c*ba*b*b*.a*")
    
  
if __name__ == "__main__":
    main()