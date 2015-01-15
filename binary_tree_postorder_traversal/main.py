# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
      if root == None:
        return []
      nodeStack = []
      nodeStack.append(root)
      vals = []
      while len(nodeStack)!=0:
        node = nodeStack[0]
        if node.left != None:
          nodeStack.insert(0,node.left)
          node.left = None
        elif node.right != None:
          nodeStack.insert(0,node.right)
          node.right = None
        else:
          nodeStack.pop(0)
          vals.append(node.val)
      return vals
      
def main():
  s = Solution()
  n1 = TreeNode(1)
  n2 = TreeNode(2)
  n3 = TreeNode(3)
  
  nx1 = TreeNode(3)
  nx2 = TreeNode(2)
  nx3 = TreeNode(4)
  nx4 = TreeNode(1)
  n2.left = n3
  n1.right = n2
  nx3.left = nx4
  nx1.left = nx2
  nx1.right = nx3
  print s.postorderTraversal(nx1)
     
if __name__ == "__main__":
    main()
    