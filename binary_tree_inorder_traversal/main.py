# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        if root == None:
          return []
        bigStack = []
        bigStack.insert(0,root)
        res = []
        while bigStack != []:
          node = bigStack[0]
          if node.left != None:
            bigStack.insert(0,node.left)
            node.left = None
          elif node.right != None:
            res.append(node.val)
            bigStack.pop(0)
            bigStack.insert(0,node.right)
          else:
            res.append(node.val)
            bigStack.pop(0)
        return res