class Solution:
    # @return a boolean
    def isMatch(self,s, p):
      #print "heres: " + s + "and " + str((s!= "") )
      fsa = self.makeFSA(p)
      print fsa
      return self.matchFSA(s,fsa)
      
    def matchFSA(self,s,fsa):
      while s != "" and len(fsa) > 0: 
        if len(fsa) == 1:
          if len(fsa[0]) > 1:
            if fsa[0][0] == ".":
              return True
            else:
              return s == fsa[0][0] * len(s)
          else:
            if len(s) > 1:
              return False
            elif fsa[0][0] == ".":
              return True
            else:
              return s == fsa[0][0]
        if len(fsa[0])>1:
 #         print "1:" + str((self.matchFSA(s[0], [fsa[0]]))) + " " + str(s[0]) + " " + str(fsa[0])
#          print "2:" + str(self.matchFSA(s[1:], fsa[1:])) 
 #         print "3:" + str(self.matchFSA(s, fsa[1:])  )
          
          return (self.matchFSA(s[0], [fsa[0]]) and self.matchFSA(s[1:], fsa)) or (self.matchFSA(s[0], [fsa[0]]) and self.matchFSA(s[1:], fsa[1:])) or self.matchFSA(s, fsa[1:])     
        else:
          return self.matchFSA(s[0], [fsa[0]]) and self.matchFSA(s[1:], fsa[1:])   
                
      return s == "" and len(fsa) == 0
      
    def makeFSA(self,p):
      i = 0
      FSA = []
      last = None
      while i < len(p):
        if p[i] not in "*":
          FSA.append([p[i]])
        else:
          FSA[-1].append('*')
        i+=1
      return FSA
          

            
          
    
        			
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
#    print s.isMatch("baccbbcbcacacbbc", "c*.*b*c*ba*b*b*.a*")
    
  
if __name__ == "__main__":
    main()