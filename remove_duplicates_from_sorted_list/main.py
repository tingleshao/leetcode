# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None:
          return head
        curr = head
        while curr.next:
          if curr.val == curr.next.val:
            curr.next = curr.next.next
          else:
            curr = curr.next
        return head