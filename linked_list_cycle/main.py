# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
      if head == None:
        return False
      rab = head
      tut = head
      tut.val = (tut.val,None)
      if rab.next == None:
        return False
      while tut.next != None and rab.next != None:
        tut = tut.next
        rab = rab.next.next
        tut.val = (tut.val,None)
        if rab == None or rab.next == None:
          return False
        if type(rab.val) is tuple and rab.val[1] == None:
          return True
      return False
        
        
    
def main():
  s = Solution()
  l1 = ListNode(1)
  l2 = ListNode(1)
  l3 = ListNode(1)
  l1.next = l2
  l2.next = l1
 # l3.next = l1
  print s.hasCycle(l1)
     
if __name__ == "__main__":
    main()
    