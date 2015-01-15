class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):

      try:
        float(s)
        return True
      except:
        return False
        
		
		
    
def main():
  s = Solution()
  print s.isNumber("0")
  print s.isNumber("0.1")
  print s.isNumber("abc")
  print s.isNumber("1 a")
  print s.isNumber("2e10")
  print s.isNumber(" ")
  print s.isNumber("2 ")
  print s.isNumber(".1")
  print s.isNumber(" 0")
  print s.isNumber(".e1")
  print s.isNumber("1e.")
  print s.isNumber("+.8")
  print s.isNumber("4e+")
  print s.isNumber(" -.")
  print s.isNumber("46.e3")
  

     
if __name__ == "__main__":
    main()