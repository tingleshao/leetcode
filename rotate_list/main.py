

# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if head == None:
          return head
        firstNode = ListNode(0)
        secondNode = ListNode(0)
        firstNode.next = head
        secondNode.next = head
        for i in xrange(k):
          if firstNode.next == None:
            firstNode.next = head
          firstNode.next = firstNode.next.next
        if firstNode.next == None:
          return head
        while firstNode.next.next != None:
          firstNode.next = firstNode.next.next
          secondNode.next = secondNode.next.next
        firstNode.next.next = head
        temp = secondNode.next.next
        secondNode.next.next = None
        return temp
        
    def rev(self,head):
      if head == None:
        return head
      tail= head
      while tail.next != None:
        tail = tail.next 
      
      self.rev(head.next)
      tail.next = head
      head.next = None
      
			
def main():
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
  
    s = Solution()
    r = s.rotateRight(n1,99)
    while r!=None:
      print r.val
      r = r.next  
  
if __name__ == "__main__":
    main()
             