
class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if s == "":
          return 0
        a = [True]
        n = self.numDecodingsH(s,a)
        if a:
          return n
        else:
          return 0
        
          
    def numDecodingsH(self,s,f):
      if '0' in s[0]:
        f[0] = False
        return 0
      if len(s) == 2 and int(s) < 27 and '0' not in s:
        return 2
      elif len(s) == 2 and int(s) < 27 and '0' in s:
        return 1
      elif len(s) == 2 and int(s) >= 27 and '0' not in s:
        return 1
      elif len(s) == 2 and int(s) >= 27 and '0' in s:
        f[0] = False
        return 0
      
      elif len(s) == 1:
        return 1
      elif int(s[:2]) < 27:
        f1 = list(f)
        f2 = list(f)
        m =  self.numDecodingsH(s[2:],f1)
        n = self.numDecodingsH(s[1:],f2)
        res = 0
        if f1[0] :
          res += m
        if f2[0]:
          res += n
        f[0] = f1[0] or f2[0]
        return res
      else:
        f1 = list(f)
        m =  self.numDecodingsH(s[1:],f1)
        f[0] = f1[0]
        if f1[0]:
          return m
          

def main():
    s = Solution()
    print s.numDecodings("12")
    print s.numDecodings("0")
    print s.numDecodings("100")
    
    
    
    
if __name__ == "__main__":
    main()