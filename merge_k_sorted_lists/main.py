# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
      dummyNode = ListNode(0)
      mn = float("Inf")
      mnind = 0
      empty = [None for j in xrange(len(lists))]
      n = len(lists)
      if lists == empty:
        return None
      for j in xrange(n):
        if lists[j] != None and lists[j].val < mn:
          mn = lists[j].val
          mnind = j
      currD = dummyNode
      dummyNode.next = lists[mnind]
      currD = currD.next
      refs = list(lists)
      refs[mnind] = refs[mnind].next
      while refs != empty:
#        print refs
        mn = float("Inf")
        mnind = 0
        for j in xrange(n):
          if refs[j] != None and refs[j].val < mn:
            mn = refs[j].val
            currD.next = refs[j]
            mnind = j
        refs[mnind] = refs[mnind].next
        currD = currD.next
            
        
      return dummyNode.next
            
        
    
          
            
      
        			
def main():
    s = Solution()
    n1 = ListNode(0)
    n2 = ListNode(1)
    t = [n1,n2]
    
    s.mergeKLists(t)
  
if __name__ == "__main__":
    main()