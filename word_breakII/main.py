class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def wordBreak(self,s,dic):
      result = ""
      solutions = []
      leng = len(s)
      possible = [True for i in xrange(leng+1)]
      self.getAllSolution(0,s,dic,leng,result,solutions,possible)
      return solutions
      
      
    def getAllSolution(self, start, s, dic, leng, result, solutions, possible):
      if start == leng:
        solutions.append(result[0:len(result)-1])
        return
      for i in xrange(start,leng):
        piece = s[start:i+1]
        if piece in dic and possible[i+1]:
          result.append(piece)
          result.append(" ")
          beforeChange = len(solutions)
          self.getAllSolution(i+1,s,dic,leng,result,solutions,possible)
          if len(solutions) == beforeChange:
            possible[i+1] = False
          result = result[:-1]
          result = result[:-len(size)]

def main():  
    s = Solution()
    print s.ladderLength("hit","cog",["hot","dot","dog","lot","log"])
    a2 = "qa"
    b2 = "sq"
    d2 = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
    print s.ladderLength(a2,b2,d2)
    


if __name__ == "__main__":
    main()