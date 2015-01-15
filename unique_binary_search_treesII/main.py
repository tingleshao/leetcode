# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
from copy import copy
class Solution:
    # @return a list of tree node
    def generateTrees(self, n):

        return self.genBSTFromLst(1,n)
      
    def genBSTFromLst(self,s,t):
      if s>t:
        return [None]
      if s == t:
        return [TreeNode(s)]
      final = []
      
      for i in xrange(s,t+1):
        left = self.genBSTFromLst(s,i-1)
        right = self.genBSTFromLst(i+1,t)
        for l in left:
          for r in right:
            tmp = TreeNode(i)
            tmp.left = l
            tmp.right = r
            final.append(tmp)
      return final

        
		
		
def main():
  s = Solution()
  print len(s.generateTrees(3))
  

     
if __name__ == "__main__":
    main()
                     
       