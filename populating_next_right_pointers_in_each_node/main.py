# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root == None:
          return 
        curr = root
        nextL = root.left
        curr.next = None
        while nextL:
          curr.left.next = curr.right
          if curr.next != None:
            curr.right.next = curr.next.left
            curr = curr.next
          else:
            curr.right.next = None
            curr = nextL
            nextL = curr.left
            
          