# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root == None:
          return 0
        return 1+max(maxDepth(root.left),maxDepth(root.right))
        
                                      
def main():
    s = Solution()
    n = int('10001000000',2)
    m = int('00101',2)
    i = 2
    j = 6
    print bin(s.updateBits(n,m,i,j))
    
    
if __name__ == "__main__":
    main()