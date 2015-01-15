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
        head = None
        prev = None
        curr = root
        while curr != None:
          while curr != None:
            if curr.left != None:
              if prev != None:
                prev.next = curr.left
              else:
                head = curr.left
              prev = curr.left
            
            if curr.right != None:
              if prev != None:
                prev.next = curr.right
              else:
                head = curr.right
              prev= curr.right
            curr = curr.next
          curr = head
          prev = None
          head = None
          
          
            
          
        
        
    
def main():
  s = Solution()
  print s.plusOne([3])
     
if __name__ == "__main__":
    main()
    