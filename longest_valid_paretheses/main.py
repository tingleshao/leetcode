class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        stack = []
        for p in xrange(len(s)):
  #        print p
          if s[p] == ")":
            if stack != []:
              if s[stack[0]] == "(":
                stack.pop(0)
              else:
                stack.insert(0,p)
            else:
              stack.insert(0,p)
          else:
            stack.insert(0,p)
        if stack == []:
          return len(s)
        print stack
        longest = 0
        a = len(s) 
        b = 0
        while stack != []:
          b = stack.pop(0)
          longest = max(longest,a-b-1)
          a = b
        longest = max(longest,a)
        return longest
              



def main():
    s = Solution()
    p1 = "(()"
    p2 = ")()())"
    print s.longestValidParentheses(p1)
    print "======"
    print s.longestValidParentheses(p2)
    
if __name__ == "__main__":
    main()