# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if root == None:
          return True
        if root.left == None and root.right == None:
          return True
        elif root.left == None:
          return self.maxDepth(root.right) <= 1
        elif root.right == None:
          return self.maxDepth(root.left) <= 1
        else: 
          return self.isBalanced(root.left) and self.isBalanced(root.right)

    def maxDepth(self,root):
      if root == None:
        return 0
      else:
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
        
				
def main():  
    s = Solution()
    


if __name__ == "__main__":
    main()