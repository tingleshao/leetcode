# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        res = ListNode(0)
        res.next = head
        cur = res
        while cur.next != None and cur.next.next != None:
          cur.next = self.swap(cur.next,cur.next.next)
          cur = cur.next.next
        return res.next
    
    def swap(self,n1,n2):
      n1.next = n2.next
      n2.next = n1
      return n2
        				
def main():  
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4

    nx1 = ListNode(1)
    nx2 = ListNode(2)
    nx1.next = nx2
    
    s = Solution()
    nn= s.swapPairs(n1)
    while nn != None:
      print nn.val
      nn = nn.next

    nnx= s.swapPairs(nx1)
    while nnx != None:
      print nnx.val
      nnx = nnx.next

if __name__ == "__main__":
    main()