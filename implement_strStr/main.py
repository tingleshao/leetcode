class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        if needle not in haystack:
            return None
        if needle=='':
            return haystack
        if needle in haystack:
            c=haystack.index(needle)
        return haystack[c:]
        
			
def main():
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
  
  
    r = s.rotateRight(n1,2)
    while r!=None:
      print r.val
      r = r.next  
  
if __name__ == "__main__":
    main()