# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
      less = ListNode(0)
      gret = ListNode(0)
      resl = ListNode(0)
      resr = ListNode(0)
      if head == None:
        return None
      if head.next == None:
        return head
      while head != None:
        if head.val < x:
          if less.next == None:
            less.next = head
            resl.next = head
            
          else:
            less.next.next = head
            less.next = less.next.next
        else:
          if gret.next == None:
            gret.next = head
            resr.next = head
            
          else:
            gret.next.next = head
            gret.next = gret.next.next
        head = head.next
      if gret.next == None:
        less.next.next = None
        return resl.next
      elif less.next == None:
        gret.next.next = None
        return resr.next
      else:
        less.next.next = resr.next
        gret.next.next = None
        return resl.next
      
        
    
def main():
  s = Solution()
  n1 = ListNode(1)
  n2 = ListNode(4)
  n3 = ListNode(3)
  n4 = ListNode(2)
  n5 = ListNode(5)
  n6 = ListNode(2)
  n1.next = n2
  n2.next = n3
  n3.next = n4
  n4.next = n5
  n5.next = n6
  ss = s.partition(n1,3)
  while ss != None:
    print ss.val
    ss = ss.next
  

if __name__ == "__main__":
    main()
                