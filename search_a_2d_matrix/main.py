class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        keys = []
        for i in matrix:
          keys.append(i[0])
        # binary search
        res = self.binSearch(keys,target,0)
        if res[0] == None:
          A =  target in matrix[res[1]]
          if res[1] != 0 :
            return target in matrix[res[1]-1] or A
          else:
            return A
        else:
          return True
        
    def binSearch(self,lst,target,offset):
      if len(lst) == 0:
        return (None,offset-1)
      if len(lst) == 1:
        if lst[0] == target:
          return (1,offset)
        return (None,offset)
      if target == lst[len(lst)/2]:
        return (1,offset)
      if target < lst[len(lst)/2]:
        return self.binSearch(lst[:len(lst)/2],target,offset)
      return self.binSearch(lst[len(lst)/2+1:],target,offset+len(lst)/2+1)

    
def main():
  s = Solution()
  m = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
  ]
  m2 = [[1],[3]]
  print s.searchMatrix(m2,4)
     
if __name__ == "__main__":
    main()
    