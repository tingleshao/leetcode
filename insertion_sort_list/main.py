# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
      pre = cursor = dummyHead = ListNode(0)
      dummyHead.next = head
      
      while cursor.next:
        if pre.next.val > cursor.next.val:
          pre = dummyHead
        while pre.next.val < cursor.next.val:
          pre = pre.next
        if pre != cursor:
          node = cursor.next
          cursor.next = node.next
          node.next = pre.next 
          pre.next = node 
        else:
          cursor = cursor.next
      return dummyHead.next
        
        
        
                            
def main():
  s = Solution()

if __name__ == "__main__":
    main()