# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
      dummyNode = ListNode(0)
      if k == 1:
        return head
      h = head
      t = head
      c = 1
      prev = dummyNode
      dummyNode.next = head
      while t != None:
   #     print "hi"
        
        while t != None and c < k:                    
          t=t.next
          c+=1
   #       print "xx"
        if t == None:
   #       print "hiii"
          break
        x = t.next
        t.next = None
        self.rev(h)
        pp = t
        if dummyNode.next == head:
          dummyNode.next = t
        prev.next = t
        prev = h
   #     print "x: " + str(x.val)
        h.next = x
        h = x
        t = x
        c = 1
      return dummyNode.next
      
      
             
    def rev(self,head):
      if head == None:
        return
      if head.next == None:
        return
      tail = head.next
      self.rev(tail)
      p = tail
      while p.next != None:
        p = p.next
      p.next = head
      head.next = None
                                      
def main():
  n1 = ListNode(1)
  n2 = ListNode(2)
  n3 = ListNode(3)
  n4 = ListNode(4)
  n5 = ListNode(5)
  n1.next = n2
  n2.next =n3
  n3.next = n4
  n4.next = n5
  
  s = Solution()
  nn = s.reverseKGroup(n1,1)
  while nn != None:
    print nn.val
    nn = nn.next

if __name__ == "__main__":
    main()