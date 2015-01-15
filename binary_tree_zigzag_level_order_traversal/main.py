# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
      res = []
      leftQueue = []
      rightQueue = []
      if root == None:
        return res
      leftQueue.insert(0,root)
      res.append([root.val])
      while len(leftQueue) != 0 or len(rightQueue) != 0:
        lst = []
        if rightQueue == []:
          while len(leftQueue) != 0:
            item = leftQueue.pop(-1)
            if item.left != None:
              rightQueue.insert(0,item.left)
              lst.append(item.left.val)
            if item.right != None:
              rightQueue.insert(0,item.right)
              lst.append(item.right.val)   
          if lst != []:
            lst.reverse()
            res.append(list(lst))
        else:  # leftQueue == []
          while len(rightQueue) != 0:
            item = rightQueue.pop(-1)
            if item.left != None:
              leftQueue.insert(0,item.left)
              lst.append(item.left.val)
            if item.left != None:
              leftQueue.insert(0,item.right)
              lst.append(item.right.val)
          if lst != []:
            res.append(list(lst))
      return res
        
				
    
def main():
  a1 = TreeNode(3)
  a2 = TreeNode(9)
  a3 = TreeNode(20)
  a4 = TreeNode(15)
  a5 = TreeNode(7)
  a1.left = a2
  a1.right = a3
  a3.left = a4
  a3.right = a5
  a6 = TreeNode(8)
  a7 = TreeNode(3)
  a2.left = a6
  a2.right = a7
  s = Solution()
  print s.zigzagLevelOrder(a1)
  ax1 = TreeNode(1)
  ax2 = TreeNode(2)
  ax1.left = ax2
  print s.zigzagLevelOrder(ax1)



if __name__ == "__main__":
    main()
                     
        