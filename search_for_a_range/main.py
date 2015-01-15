class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        index= self.binSearch(A,0,len(A)-1,target)
        result = [-1,-1]
        if index != -1:
          left = index
          right = index
          result[0] = left
          result[1] = right
          while left != -1:
            left  = self.binSearch(A, 0, left-1, target)
            if left!= -1:
              result[0] = left
          while right != -1:
            right = self.binSearch(A,right+1,len(A)-1,target)
            if right != -1:
              result[1] = right
        return result
    def binSearch(self,A,l,r,target):
      while l <= r:
        mid = l + (r-l) / 2
        if A[mid] < target: 
          l = mid+1
        elif A[mid] > target:
          r = mid-1
        else:
          return mid
      return -1
 #       if len(A) == 0:
#          return [-1,-1]
#        if len(A) == 1:
 #         if A[0] == target:
  #          return [offset,offset]
   #       else:
    #        return [-1,-1]
#        if len(A) == 2:
 #         if A[0] == target:
  #          if A[1] == target:
   #           return [offset,offset+1]
    #        else:
     #         return [offset,offset]
      #    elif A[1] == target:
#            return [offset +1,offset+1]
 #         else:
  #          return [-1,-1]
   #     while(l<r):
    #       print "foo"
     #      mid = (r-l) / 2
      #     if A[mid] < target:
      #       print mid 
#             return self.binSearch(A[mid+1:],0,(r-mid)-1,target,offset+mid+1)
  #          elif A[mid] > target:
     #      print mid 
   #          return self.binSearch(A[:mid],0,mid,target,offset)
    #       else:
     #        b = self.binSearch(A[mid+1:],0,(r-mid)-1,target,offset+mid+1)
      #       a = self.binSearch(A[:mid],0,mid,target,offset)
       #      print b
        #     print mid 
       #      print "a: " + str(a)
        #     print "b: " + str(b)
         #    if a == [-1,-1]:
          #     return b
           #  if b == [-1,-1]:
            #   return a
             #return [a[0],b[1]]
          
             
          
    
def main():
  s = Solution()
  n = s.searchRange([5, 7, 7, 8, 8, 10],8)
  n2 = s.searchRange([1,2,3,3,3,3,4,5,9],3)
  n3 = s.searchRange([2,2],2)
  print "  -----------  "
  
  n4 = s.searchRange([1,2,3],2)
  
  print n
  print n2
  print n3
  print n4
     
if __name__ == "__main__":
    main()