# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
      bigStack = []
      if root == None:
        return []
      bigStack.append(root)
      result = []
      while bigStack != []:
        top = bigStack.pop(0)
        result.append(top.val)
        if top.right != None:
          bigStack.insert(0,top.right)
          top.right = None
        if top.left != None:
          bigStack.insert(0,top.left)
          top.left = None
        
      return result
        
        
def main():  
    s = Solution()
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.right = n2
    n2.left = n3
    print s.preorderTraversal(n1)

if __name__ == "__main__":
    main()