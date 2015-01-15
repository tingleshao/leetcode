# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
      if root == None:
        return 0
      return self.sumR(root,0)
        
        
        
    def sumR(self,root,x):
      if root.left == None and root.right == None:
        return 10*x + root.val
      val = 0
      if root.left != None:
        val += self.sumR(root.left, 10*x+root.val)
      if root.right != None:
        val += self.sumR(root.right, 10*x+root.val)
      return val
        
            
            
        
        
    
def main():
  s = Solution()
  n1 = TreeNode(1)
  n2 = TreeNode(2)
#  n3 = TreeNode(3)
  n1.left = n2
 # n1.right = n3
  print s.sumNumbers(n1)

     
if __name__ == "__main__":
    main()