# Definition for singly-linked list.
class ListNode:
      def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if l1 == None:
          return l2
        if l2 == None:
          return l1
        
        head1 = ListNode(0)
        curr = head1
        curr1 = l1
        curr2 = l2
        while curr1 != None and curr2 != None:
          val1 = curr1.val
          val2 = curr2.val
          if val1 >= val2:
            curr.next = curr2
            curr2 = curr2.next
          else:
            curr.next = curr1
            curr1 = curr1.next
          curr = curr.next
        if curr2 == None:
          curr.next = curr1
        else:
          curr.next = curr2
        return head1.next
             
        
        
        				
def main():  
    s = Solution()
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n6 = ListNode(6)
    n1.next = n3
    n2.next = n4
    n3.next = n5
    n4.next = n6
    nn = s.mergeTwoLists(n2,n1)
    while nn != None:
      print nn.val
      nn = nn.next
    
    
    


if __name__ == "__main__":
    main()