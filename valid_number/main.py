class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):

      if s == "":
        return False
      si = 0
      if s[0] == " ":
        while si < len(s) and s[si] == " ":
          si+=1
   #   print "si: " + str(si)
      sei = 0
      
      if s[-1] == " ":
        sei = 1
        while sei <= len(s) and s[-sei] == " ":
          sei += 1
      s = s[si:len(s)-sei+1]
 #     print s
 #     print len(s)
      seen_d = False
      seen_b = False
      seen_e = False
      seen_s = False
      just_seen_d = False
      seen_p = False
      if s == "":
        return False
    #  print len(s)
      
      if (not s[0].isdigit()) and s[0] != "-" and s[0] != "." and s[0] != "+":
        return False
      elif len(s) == 1:
        if s[0] == "-" or s[0] == "." or s[0] == "+":
          return False
        else:
          return True
      elif s[0] == "-":
        seen_b = True
      elif s[0] == "+":
        seen_p = True
      elif s[0] == ".":
        seen_d = True
      curr = 1
      while curr<len(s):
        if not s[curr].isdigit():
          if s[curr] not in [".","e","-","+"]:
            return False
          else:
            if s[curr] == "+" or s[curr] == "-":
              if s[curr-1] != "e" or curr == len(s)-1:
                return False
            if s[curr] == "e":
              if seen_e:
                return False
              elif curr == len(s)-1:
                return False
              elif s[curr-1] == ".":
                if curr == 1:
                  return False
              else:
                seen_e = 1
            if s[curr] == ".":
              if seen_d:
                return False
              elif curr == len(s)-1 and (s[-2] == "e" or s[-2] == "-" or s[-2] == "+") :
                return False
              else:
                seen_d = 1
        curr += 1
      return True
        
		
		
    
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