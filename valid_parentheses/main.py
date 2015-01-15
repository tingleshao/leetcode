class Solution:
    # @return a boolean
    def isValid(self, s):
        c1 = 0
        c2 = 0
        c3 = 0
        stateStack = []
        for x in s:
          if x == "(":
            stateStack.insert(0,1)
            c1 += 1
   #         print "1"
          elif x == "[":
            stateStack.insert(0,2)
            c2 += 1
    #        print "2"
            
          elif x == "{":
            stateStack.insert(0,3)
            c3 += 1
     #       print "3"
            
          elif x == ")":
            if len(stateStack) == 0:
              return False
            state = stateStack[0]
            if state == 2 or state == 3:
              return False
            c1 -= 1
            if c1 < 0:
              return False
            stateStack.pop(0)
              
    #        print "4"
              
          elif x == "]":

            if len(stateStack) == 0:
              return False
            state = stateStack[0]
            if state == 1 or state == 3:
              return False
            stateStack.pop(0)
              
            c2 -= 1
            if c2 < 0:
              return False
    #        print "5"
     #       
          elif x == "}":

            if len(stateStack) == 0:
              return False
            state = stateStack[0]

            if state == 1 or state == 2:
              return False
            c3 -= 1
            stateStack.pop(0)
            if c3 < 0:
              return False
     #       print "6"
            
        if len(stateStack) != 0:
          return False
        return True
          
				 
def main():
  a = "()"
  b = "[]"
  c = "(]"
  d = "([)]"
  e = "([])"
  f = "[{()}]"
  s = Solution()
  print s.isValid(a)
  print s.isValid(b)
  print s.isValid(c)
  print s.isValid(d)
  print s.isValid(e)
  print s.isValid(f)
  
  
  
     
if __name__ == "__main__":
    main()