
class ListNode:
  def __init__(self,x):
    self.val = x
    self.next = None

class Solution:
  def reorderList(self,head):
    l = 0
    curr = head
    while curr != None:
      curr = curr.next
      l += 1
    if l == 0:
      return
    if l == 1:
      return 
    a, b = self.splitList(head)
    b = self.reverseList(b)
    head = self._mergeLists(a,b)
  
  def reverseList(self,head):
    last = None
    curr = head
    
    while curr:
      nextnode = curr.next
      curr.next = last
      last = curr
      curr = nextnode
      
    return last

  def splitList(self,head):
    fast = head
    slow = head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next
      fast = fast.next
      
    middle = slow.next
    slow.next = None
    return head, middle
    
  def _mergeLists(self,a,b):
    tail = a
    head = a
    a = a.next
    while b:
      tail.next = b
      tail = tail.next
      b = b.next
      if a:
        a,b = b,a
    return head

        			
def main():
    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(3)
    a4 = ListNode(4)
    a1.next = a2
    a2.next = a3
    a3.next = a4
    s = Solution()
    s.reorderList(a1)
    while a1!= None:
      print a1.val
      a1 = a1.next
    
    
  
if __name__ == "__main__":
    main()