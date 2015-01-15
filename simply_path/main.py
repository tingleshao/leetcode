class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        simp = ""
        stack = []
        
        self.simplify(path,stack)
        if stack == []:
          return "/"
        stack.reverse()
        for item in stack:
          if len(simp) == 0 or simp[-1] != "/" :
            simp+= "/"
          
          simp = simp + item
        return simp
        
        
    def simplify(self,path,stack):
      if path == "/" or path == "":
        return
      j = 1
      between = ""
      while j < len(path):
        if path[j] == "/":
          break
        between = between + path[j]
        j += 1
      
      if between == "." or between == "":
        self.simplify(path[j:],stack)
      elif between == "..":
        if len(stack) > 0:
          stack.pop(0)
        self.simplify(path[j:],stack)
      else:
        stack.insert(0,between)
        self.simplify(path[j:],stack)


def main():
    p0 = "/home/"
    p1 = "/a/./b/../../c/"
    p2 = "///"
    p3 = "/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///"
    s = Solution()
    print s.simplifyPath(p0)
    print s.simplifyPath(p1)
    print s.simplifyPath(p2)
    print s.simplifyPath(p3)
    
    
    
  
if __name__ == "__main__":
    main()