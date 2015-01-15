# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        bigStack = []
        if root == None:
          return 0
        digits = []
        totalsum = 0
        bigStack.insert(0,[root,0])
        while len(bigStack) != 0:
          nodex = bigStack[0]
          node = nodex[0]
          if len(bigStack) == 1:
            digits = []
            digits.append(node.val)
          if node.left != None:
            bigStack.insert(0,[node.left,0])
            digits.append(node.left.val)
            node.left = None
          elif node.right != None:
            bigStack.insert(0,[node.right,0])
            digits.append(node.right.val)
            node.right = None
          else:
            if nodex[1] == 0:
              ssum = 0
              for i in xrange(len(digits)):
                ssum += digits[i] *(10**(len(digits)-i-1))
              totalsum += ssum
            bigStack.pop(0)
          nodex[1] = 1
        return totalsum
        
            
            
        
        
    
def main():
  s = Solution()
  n1 = TreeNode(1)
  n2 = TreeNode(2)
#  n3 = TreeNode(3)
  n1.left = n2
 # n1.right = n3
  print s.sumNumbers(n1)

     
if __name__ == "__main__":
    main()