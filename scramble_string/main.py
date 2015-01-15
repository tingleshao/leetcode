
class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
       if s1 == s2 == None:
         return False
       if s1 == s2:
         return True
       if len(s1) != len(s2):
         return False
       if sorted(s1) != sorted(s2):
         return False
       for i in xrange(1,len(s1)):
         if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]):
           return True
         if self.isScramble(s1[:i],s2[len(s1)-i:]) and self.isScramble(s1[i:],s2[:len(s1)-i]):
           return True
       return False



def main():
  s = Solution()
  
  print s.isScramble("rgtae","great")
  print s.isScramble("abcd","bdac")
  print s.isScramble("abc","bca")
  print s.isScramble("abc","cab")
  s1 = "abc"
  s2 = "cab"
  i  = 2
  print s.isScramble(s1[:i],s2[len(s1)-i:]) and s.isScramble(s1[i:],s2[:len(s1)-1]):


if __name__ == "__main__":
    main()
             