# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        bigStack = []
        bigStack.insert(0,root)
        if root == None:
          return False
        if root.left == None and root.right == None and root.val == sum:
          return True
        while len(bigStack) > 0:
          node = bigStack[0]
  #        print node.val
          if node.left != None:
            node.left.val = node.left.val + node.val
        #    print node.left.val
            if node.left.left == node.left.right == None:
              if node.left.val == sum:
                return True
              else:
                node.left = None
            else:
              bigStack.insert(0,node.left)
              node.left = None
          elif node.right != None:
            node.right.val = node.right.val + node.val 
        #    print node.right.val
            if node.right.left == node.right.right == None:
              if node.right.val == sum:
                return True
              else:
                node.right = None
            else:
              bigStack.insert(0,node.right)
              node.right = None
          else:
            
            bigStack.pop(0)
          
        return False
            
				
  
def main():
  s = Solution()
  n1 = TreeNode(5)
  n2 = TreeNode(4)
  n3 = TreeNode(8)
  n4 = TreeNode(11)
  n5 = TreeNode(13)
  n6 = TreeNode(4)
  n7 = TreeNode(7)
  n8 = TreeNode(2)
  n9 = TreeNode(1)
  n6.right = n9
  n4.left = n7
  n4.right = n8
  n3.left = n5
  n3.right = n6
  n2.left = n4
  n1.left = n2
  n1.right = n3
  
  
  print s.hasPathSum(n1,22)
     
if __name__ == "__main__":
    main()
    