class Solution:
    # @param an integer
    # @return a list of string
    pares = []
    def generateParenthesis(self, n):
        self.pares = []
        p = ""
        self.genParet(n,n,p)
        return self.pares
    
    def genParet(self,l,r,p_in):
        if l == 0:
            p = p_in + ")" * r
            self.pares.append(p)
            return 
        if l == r:
            p = p_in + "("
            self.genParet(l-1,r,p)
            return
        else:
            p1 = p_in + "("
            self.genParet(l-1,r,p1)
            p2 = p_in + ")"
            self.genParet(l,r-1,p2)
            return
    
def main():
  s = Solution()
  print s.generateParenthesis(2)
     
if __name__ == "__main__":
    main()
    