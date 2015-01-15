# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if l1 == None:
          return l2
        if l2 == None:
          return l1
        curr1 = l1
        curr2 = l2
        res = ListNode(0)
        reshead = res
        curry = 0
        white = ListNode(0)
        
        while True:
          sm = curr1.val + curr2.val + curry
          
          if sm <= 9:
            res.val = sm
            curry = 0
          else:
            res.val = sm % 10
            curry = 1
          nxt = ListNode(0)
          curr1 = curr1.next
          curr2 = curr2.next
          if curr1 == None and curr2 == None:
            if curry == 1:
              nxt.val = 1
              res.next = nxt
            white.next = None
            return reshead
          if curr1 == None:
            curr1 = white
          if curr2 == None:
            curr2 = white
          res.next = nxt             
          res = nxt
          
            


def main():
  s = Solution()
  l1 = ListNode(2)
  l2 = ListNode(4)
  l3 = ListNode(3)
  l4 = ListNode(5)
  l5 = ListNode(6)
  l6 = ListNode(4)
  l1.next = l2
  l2.next = l3
  l4.next = l5
  l5.next = l6
  lx1 = ListNode(5)
  lx2 = ListNode(5)
  lxx1 = ListNode(1)
  lxx2 = ListNode(8)
  lxx3 = ListNode(0)
  lxx1.next = lxx2
  nn = s.addTwoNumbers(l1,l4)
#  nn = s.addTwoNumbers(lx1,lx2)
#  nn = s.addTwoNumbers(lxx1,lxx3)
  
  while nn != None:
    print nn.val
    nn = nn.next


if __name__ == "__main__":
    main()