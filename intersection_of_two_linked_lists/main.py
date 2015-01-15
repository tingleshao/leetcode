# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        lenA = 0
        lenB = 0
        currA = headA
        currB = headB
        if not headA and not headB:
          return None
        while currA:
          currA = currA.next
          lenA += 1
        while currB:
          currB = currB.next
          lenB += 1
        if lenB > lenA:
          temp = headB
          headB = headA
          headA = temp
        currA = headA
        currB = headB
        lenDiff = abs(lenA - lenB)
        while lenDiff > 0:
          currA = currA.next
          lenDiff -= 1
        while currA:
          if currA == currB:
            return currA
          currA = currA.next
          currB = currB.next
        return None
          
          
          
          