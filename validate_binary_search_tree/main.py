# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
      return self.isValidBSTHelp(root.left,-1*float("Inf"),root.val) and self.isValidBSTHelp(root.right,root.val,float("Inf"))
       
        
        
        
    def isValidBSTHelp(self,root,mn,mx):
        if root == None:
          return True
        return mn < root.val < mx and self.isValidBSTHelp(root.left,mn,root.val) and self.isValidBSTHelp(root.right,root.val,mx)
       
    
                    
            
def main():
  s = Solution()
  print s.addBinary("11","1")

if __name__ == "__main__":
    main()