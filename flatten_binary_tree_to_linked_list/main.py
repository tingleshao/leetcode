# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        while root != None:
          if root.left != None:
            ptr = root.left
            while ptr.right != None:
              ptr = ptr.right
            ptr.right = root.right
            root.right = root.left
            root.left = None
          root = root.right
          
          
          
          
    
def main():
  s = Solution()
  n1 = TreeNode(0)
  s.flatten(n1)
  print n1.val

     
if __name__ == "__main__":
    main()
				
