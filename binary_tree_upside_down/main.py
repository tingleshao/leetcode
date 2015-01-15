# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return root of the upside down tree
    def upsideDownBinaryTree(self, root):
        if not root:
          return None
        if root.right == None:
          return root
        resRt = None
        resRtleft = None
        while root:
          newResRt = TreeNode(root.val)
          newResRt.right = resRt
          newResRt.left = resRtleft
          resRtleft = root.right
          resRt = newResRt
          root = root.left
        return resRt
        