# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def detectCycle(self, head):
      count = 0 
      if head == None:
        return None
      tut = head
      tut.val = (tut.val,count)
      count += 1
      while tut.next != None:
        if type(tut.next.val) is tuple:
          tut.next.val = tut.next.val[0]
          return tut.next
        tut = tut.next
        tut.val = (tut.val,count)
      return None
        
        
    
def main():
  s = Solution()
  l1 = ListNode("l1")
  l2 = ListNode("l2")
  l3 = ListNode("l3")
  l1.next = l2
  l2.next = l1
 # l3.next = l1
  print s.detectCycle(l1).val
     
if __name__ == "__main__":
    main()
    