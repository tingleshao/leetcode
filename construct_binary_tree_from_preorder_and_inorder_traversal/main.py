# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        i = 0 # index for preorder
        j = 0 # index for inorder
        dummyNode = TreeNode(float(Inf))
        pp = None
        bigStack = []
        bigStack.insert(0,dummyNode)
        while j < len(inorder):
          if bigStack[0].val == inorder[j]:
            pp = bogStack.pop(0)
            j+=1
          elif pp != None:
            newNode = TreeNode(preorder[i])
            pp.right = newNode
            pp = None
            bigStack.insert(0,newNode)
            i+=1
          else:
            newNode = TreeNode(preorder[i])
            bigStack.left = newNode
            bigStack.insert(0,newNode)
            i+=1
        return root.left