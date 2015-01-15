# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return a tree node
      
    def recoverTree(self, root):

      self.first = None
      self.second = None
      self.pre = None
      self.recoverTree2(root)
  #    print self.first.val
  #    print self.second.val
      temp = self.first.val
      self.first.val = self.second.val
      self.second.val = temp

     # print self.first.val
   #   print self.second.val
   #   print root.val
      return root
      
    
    def recoverTree2(self,root):
      
      if root == None:
        return
      if root.left != None:
        self.recoverTree2(root.left)
      if self.pre != None and self.pre.val > root.val:
        if self.first == None:
          self.first = self.pre
        self.second = root
        
      self.pre = root
      if root.right != None: 
        self.recoverTree2(root.right)
        		

def main():
  s = Solution()
  n1 = TreeNode(0)
  n2 = TreeNode(1)
  n1.left = n2
  s.recoverTree(n1)
#  print n1.left.val



if __name__ == "__main__":
    main()
             