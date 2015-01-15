# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
      if len(lists) == 0:
        return None
      dummy = ListNode(0)
      tail = dummy
      queue = []
      
      for i in            
      
class pQueue:
  def 
        			
def main():
    s = Solution()
    n1 = ListNode(0)
    n2 = ListNode(1)
    t = [n1,n2]
    
    s.mergeKLists(t)
  
if __name__ == "__main__":
    main()