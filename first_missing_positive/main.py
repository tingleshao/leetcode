class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
      if A == []:
        return 1
      array = []
      for item in A:
        if item > 0:
          array.append(item)
      N = len(array)
#      print "len: " +str(N)
      #Pass 1, move every value to the position of its value
      for cursor in range(1,N+1): 
          target = array[cursor-1]
          while target > 0 and target < N+1 and target != array[target-1]:
              new_target = array[target-1]
              array[target-1] = target
              target = new_target
      print array
              
              
      #Pass 2, find first location where the index doesn't match the value
      for cursor in range(1,N+1):
          if array[cursor-1] != cursor:
              return cursor
      return N+1
			


def main():
  s = Solution()
  a1 = [1,2,0]
  a2 = [3,4,-1,1]
  a3 = [1000,-1]
  a4 = [-5,1000]
  a5 = [1]
  a6 = [0]
  print s.firstMissingPositive(a1)
  print s.firstMissingPositive(a2)
  print s.firstMissingPositive(a3)
  print s.firstMissingPositive(a4)
  print s.firstMissingPositive(a5)

  print s.firstMissingPositive(a6)
  
  
  

if __name__ == "__main__":
    main()
             