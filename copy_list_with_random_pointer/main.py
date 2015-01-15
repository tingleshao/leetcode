# Definition for singly-linked list with a random pointer.
class RandomListNode:
     def __init__(self, x):
         self.label = x
         self.next = None
         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head == None:
          return None
        p = head
        while True:
          q = p.next 
          p.next = RandomListNode(p.val)
          p.next.next = q
          p = q
          if p == None:
            break
        p = head
        while True:
          if p.random != None:
            p.next.random = p.random.next
          p = p.next.next
          if p == None:
            break
        p = head
        r = head.next
        q = r
        while True:
          p.next = q.next
          p = p.next
          if p == None:
            break
          q.next = p.next
          q = q.next
        return r
          




def main():
  s = Solution()
  print s.copyRandomList(head)



if __name__ == "__main__":
    main()
             