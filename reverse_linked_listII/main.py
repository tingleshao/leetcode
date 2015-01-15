# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if head == None:
          return None
        dummyNode = ListNode(0)
        dummyNode.next = head
        curr = ListNode(0)
        curr.next = head
        for i in xrange(m-1):
          curr.next = curr.next.next
        curr2 = ListNode(0)
        curr2.next = curr.next
        for j in xrange(n-m):
          curr2.next = curr2.next.next
        tail = curr2.next.next 
        pp = curr2.next
        curr2.next.next = None
        self.rev(curr.next)
      
     #   while pp != None:
    #      print pp.val
     #     pp = pp.next
        if m == 1:
          curr2.next = pp
          for j in xrange(n-m):
            curr2.next = curr2.next.next
          curr2.next.next = tail
          return pp
        
        for i in xrange(m-2):
          head = head.next
        head.next = pp
        curr2.next = pp
        for i in xrange(n-m):
          curr2.next = curr2.next.next
        curr2.next.next = tail
        return dummyNode.next
        
    def rev(self,head):
      if head == None:
        return 
      if head.next == None:
        return 
      else:
        revs = head.next
        self.rev(revs)
        head.next = None
        revs.next = head
            
def main():
  s = Solution()
  n1 = ListNode(1)
  n2 = ListNode(2)
  n3 = ListNode(3)
  n4 = ListNode(4)
  n5 = ListNode(5)
  n1.next = n2
  n2.next = n3
  n3.next = n4
  n4.next = n5
  
  nx1 = ListNode(3)
  nx2 = ListNode(5)
  nx1.next = nx2
  nn = s.reverseBetween(n1,2,4)
  while nn != None:
    print nn.val
    nn = nn.next
  print "========"
  nn2 = s.reverseBetween(nx1,1,1)
  while nn2 != None:
    print nn2.val
    nn2 = nn2.next



if __name__ == "__main__":
    main()
                     
        