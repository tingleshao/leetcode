# Definition for a  binary tree node
import math

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        if root == None:
          return []
        bigStack = []
        visitQueue = []
        visitQueue.append((root,1))
        bigDict = {}
        bigDict[1]= [root.val]
        while 0 != len(visitQueue):
          node = visitQueue.pop(0)
          if node[0].left != None:
            visitQueue.append((node[0].left,node[1]+1))
            if bigDict.has_key(node[1]+1):
              bigDict[node[1]+1].append(node[0].left.val)
            else:
              bigDict[node[1]+1] = [node[0].left.val]
          if node[0].right != None:
            visitQueue.append((node[0].right,node[1]+1))
            if bigDict.has_key(node[1]+1):
              bigDict[node[1]+1].append(node[0].right.val)
            else:
              bigDict[node[1]+1]=[node[0].right.val]
        
        level = len(bigDict)
        bigLst  = []
        for i in xrange(level):
          bigLst.append(bigDict[i+1])
 #       bigLst.reverse()
        return bigLst
        
        
  
        
        
    
def main():
  s = Solution()
  root = TreeNode(3)
  n3 = TreeNode(20)
  n6 = TreeNode(15)
  n7 = TreeNode(7)
  n2 = TreeNode(9)
  n3.left = n6
  n3.right = n7
  root.left = n2
  root.right = n3
  print s.levelOrderBottom(root)
     
if __name__ == "__main__":
    main()
    