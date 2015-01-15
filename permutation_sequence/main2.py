import math
class Solution:

 def getPermutation(self, n, k):
    array = range(1, n + 1)
    k = (k % math.factorial(n)) - 1
    permutation = []
    for i in xrange(n - 1, -1, -1):
        idx, k = divmod(k, math.factorial(i))
        print idx, k, math.factorial(i), i
        permutation.append(array.pop(idx))

    return "".join(map(str, permutation))
    
def main():
  s = Solution()
  n = 3
  k = 3
  print s.getPermutation(n,k)
#  print s.getPermutation(9,273815)
  
  
  
if __name__ == "__main__":
    main()
             