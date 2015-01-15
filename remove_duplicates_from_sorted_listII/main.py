# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
      vdict = []
      ddict = []
      if head == None:
        return None
      dummyNode = ListNode(0)
      res = dummyNode
      c = head
      while c != None:
        if not c.val in vdict:
          vdict.append(c.val)
          c = c.next
        else:
          ddict.append(c.val)
          while c != None and c.val in vdict:
            c = c.next
      for j in vdict:
        if j not in ddict:
          newNode = ListNode(j)
          dummyNode.next = newNode
          dummyNode = dummyNode.next
      return res.next
          
          
                
                            
def main():
  a1 = ListNode(1)
  a2 = ListNode(2)
  a3 = ListNode(3)
  a4 = ListNode(3)
  a5 = ListNode(4)
  a6 = ListNode(4)
  a7 = ListNode(5)
  a1.next = a2
  a2.next = a3
  a3.next = a4
  a4.next = a5
  a5.next = a6
  a6.next = a7
  ax1 = ListNode(1)
  ax2 = ListNode(1)
  ax3 = ListNode(1)
  ax4 = ListNode(2)
  ax5 = ListNode(3)
  ax1.next = ax2
  ax2.next = ax3
  ax3.next = ax4
  ax4.next = ax5
  s = Solution()
  aa = s.deleteDuplicates(a1)
  while aa != None:
    print aa.val
    aa = aa.next

  aa = s.deleteDuplicates(ax1)
  while aa != None:
    print aa.val
    aa = aa.next
if __name__ == "__main__":
    main()