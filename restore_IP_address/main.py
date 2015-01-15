class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        if len(s) > 12 or len(s) < 4:
          return []
        res = []
        for i in xrange(1,4):
          if i < len(s):
            part1 = s[:i]
            if -1 < int(part1) < 256 and (not (len(part1 )>1 and int(part1[0]) == 0)):
              for j in xrange(i+1,i+4):
               if j < len(s):
                 part2 = s[i:j]
                 if -1 < int(part2) < 256 and (not (len(part2)>1 and int(part2[0]) == 0)):
                   for k in xrange(j+1,j+4):
                     if k < len(s):
                       
                       part3 = s[j:k]
                       if -1 < int(part3) < 256 and (not (len(part3) > 1 and part3[0] == '0')):
                         part4 = s[k:]
                         if -1 < int(part4) < 256 and (not (len(part4 )> 1 and part4[0] == '0')):
                           res.append(".".join([part1,part2,part3,part4]))
        return res
                           
        
        
                			
def main():
    s = Solution()
    print s.restoreIpAddresses("25525511135")
    print s.restoreIpAddresses("010010")
    
  
if __name__ == "__main__":
    main()