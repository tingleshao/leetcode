# Definition for a  binary tree node
class TreeNode:
       def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
      if len(inorder) == 0:
        return None
      bigStack = []
      ino = list(inorder)
      post = list(postorder)
      curr = None
      root = TreeNode(post[-1])
      bigStack.insert(0,root)
      post.pop(-1)
      curr = bigStack[0]
      while True:
        if ino[-1] == bigStack[0].val:
          curr = bigStack[0]
          bigStack.pop(0)
          ino.pop(-1)
          if len(ino) == 0:
            break
          if len(bigStack) != 0:
            if ino[-1] == bigStack[0].val:
              continue
          newNode = TreeNode(post[-1])
          curr.left = newNode
          curr = newNode
          bigStack.insert(0,newNode)
          post.pop(-1) 
        else:
          newNode = TreeNode(post[-1])
          curr.right = newNode
          bigStack.insert(0,newNode)
          post.pop(-1)
      return root		
    
def main():
  s = Solution()
  print s.buildTree([2,1],[2,1])



if __name__ == "__main__":
    main()
                     
        