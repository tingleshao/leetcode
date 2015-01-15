# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        arr = []
        while head != None:
          arr.append(head.val)
          head = head.next
        root = self.sortedArrToBST(arr,0,len(arr)-1)
        return root
        
    def sortedArrToBST(self,arr,start,end):
        if start > end:
          return None
        mid = ( end-start ) / 2 + start
        node = TreeNode(arr[mid])
        node.left = self.sortedArrToBST(arr,start,mid-1)
        node.right = self.sortedArrToBST(arr,mid+1,end)
        return node
          
          
            
            
		
		
def main():
  n1 = ListNode(1)
  n2 = ListNode(3)
  n1.next = n2
  s = Solution()
  print s.sortedListToBST(n1).val
  

     
if __name__ == "__main__":
    main()
                     
       