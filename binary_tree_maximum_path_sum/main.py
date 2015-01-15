# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        if root == None:
          return 0
        mx = [root.val]
        self.recNodes(root, mx)
        return mx[0] 
        		
    def recNodes(self, node, mx):
      numl = 0
      numr = 0
      if node.left != None:
        numl = self.recNodes(node.left)
      if node.right != None:
        numr = self.recNodes(node.right)
        
      value = node.val
      sumWhole = self.checkMax(value, numl+numr, mx)
      if numl > 0:
        sumLeft = checkmax(value,numl, mx)
      else:
        sumLeft = value
      if numlr> 0:
        sumRight = checkmax(value,numr, mx)
      else:
        sumRight = value
      return max(sumLeft,sumRight), mx
      
    def checkMax(self, val, sm, mx):
      if sm > 0:
        sm += val
      else:
        sm = val
      if sm > mx[0]:
        mx[0] = sm
      return sm
def main():
    
    s = Solution()
  
if __name__ == "__main__":
    main()