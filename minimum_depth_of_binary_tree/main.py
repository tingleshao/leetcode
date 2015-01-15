# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        minD = 1
        if root == None:
          return 0
        if root.left == root.right == None:
          return minD
        elif root.left != None:
          if root.right == None:
            return 1 + self.minDepth(root.left)
          else:
            return 1 + min(self.minDepth(root.left),self.minDepth(root.right))
        else:
          return 1+ self.minDepth(root.right)
            
        
        
    
def main():
  s = Solution()
  n1 = TreeNode(1)
#  n2 = TreeNode(2)
#  n3 = TreeNode(3)
#  n1.left = n2
#  n1.right = n3
  print s.minDepth(None)

     
if __name__ == "__main__":
    main()