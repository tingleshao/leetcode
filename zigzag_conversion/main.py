class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1:
          return s
        if nRows == 0:
          return ""
        if len(s) <= nRows:
          return s
        lets = []
        for i in xrange(nRows):
          lets.append(s[i])
        counts = nRows - 1
        down = False
        i = nRows 
        while True:
          if i >= len(s):
            res = ""
            for item in lets:
              res = res + item 
            return res
          
          if counts == 0:
            down = True
          if counts == nRows-1:
            down = False
          if down:
            counts += 1
          else:
            counts -= 1
          lets[counts] = lets[counts] + s[i]
            
          i += 1
        

def main():
  s = Solution()
  t = "PAYPALISHIRING"
  print s.convert(t,3)



if __name__ == "__main__":
    main()
                
          
        
        