# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
      bigStack = []
      res = []
      if root == None:
        return res
      bigStack.insert(0,root)
      currLst = []
      
      currLst.append(root.val)
      currSum = root.val
      if currSum == sum and root.left == root.right == None:
        res.append(currLst)
        return res
      while len(bigStack) != 0:
        node = bigStack[0]
        if node.left != None:
          bigStack.insert(0,node.left)
          currLst.insert(0,node.left.val)
          currSum += node.left.val
          if currSum == sum:
            if node.left.left == node.left.right == None:
              currCP = list(currLst)
              currCP.reverse()
              res.append(currCP)
          node.left = None
        elif node.right != None:
          bigStack.insert(0,node.right)
          currLst.insert(0,node.right.val)
          currSum += node.right.val
          if currSum == sum:
            if node.right.left == node.right.right == None:
              currCP = list(currLst)
              currCP.reverse()
              res.append(currCP)
          node.right = None
        else:
          bigStack.pop(0)
          currLst.pop(0)
          currSum -= node.val
      return res
				
        
				
def main():
  s = Solution()
  n1 = TreeNode(5)
  n2 = TreeNode(4)
  n3 = TreeNode(8)
  n4 = TreeNode(11)
  n5 = TreeNode(13)
  n6 = TreeNode(4)
  n7 = TreeNode(7)
  n8 = TreeNode(2)
  n9 = TreeNode(5)
  n10 = TreeNode(1)
  n6.left = n9
  n6.right = n10
  n4.left = n7
  n4.right = n8
  n3.left = n5
  n3.right = n6
  n2.left = n4
  n1.left = n2
  n1.right = n3
  
  nx1 = TreeNode(1)
  nxx1 = TreeNode(1)
  nxx2 = TreeNode(2)
  nxx1.left = nxx2
  
  nxxx1 = TreeNode(1)
  nxxx2 = TreeNode(2)
  nxxx3 = TreeNode(3)
  nxxx4 = TreeNode(4)
  nxxx5 = TreeNode(5)
  nxxx1.left = nxxx2
  nxxx2.left = nxxx3
  nxxx3.left = nxxx4
  nxxx4.left = nxxx5
  print s.pathSum(n1,22)
  
  print s.pathSum(nx1,1)
  print s.pathSum(nxx1,1)
  print s.pathSum(nxxx1,6)
  
  
  
  
  

     
if __name__ == "__main__":
    main()