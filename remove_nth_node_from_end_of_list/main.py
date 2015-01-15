# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        fasthead = head
        slowhead = head
        before = ListNode(0)
        before.next = slowhead
        if fasthead.next == None:
          return None
                    
        
        for i in xrange(n):
          fasthead = fasthead.next
          
        while fasthead!= None:
          fasthead = fasthead.next
          before = slowhead
          
          slowhead = slowhead.next
     #     print before.val
          
        tmp = slowhead
        before.next = slowhead.next
        tmp.next = None
        if head == tmp:
          return before.next
        
        return head
          
          
    
def main():
  s = Solution()
  n1 = ListNode(1)
  n2 = ListNode(2)
  n3 = ListNode(3)
  n1.next = n2
  #n2.next = n3
  n = s.removeNthFromEnd(n1,2)
  while n != None:
    print n.val
    n = n.next
     
if __name__ == "__main__":
    main()
    