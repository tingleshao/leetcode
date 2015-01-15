class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
      n = len(A)
      m = len(B)
      if n > m:
        return self.findMedianSortedArrays(B,A)
      k = (n+m-1)/2
      l = 0
      r = min(k,n)
      while l < r:
        midA = (l+r)/2
        midB = k-midA
        if midB > k or A[midA] < B[midB]:
          l = midA + 1
        else:
          r = midA
      if l > 0:
        first = A[l-1]
      else:
        first = -1*float("Inf")
      if k-l >= 0:
        second = B[k-l]
      else: 
        second = -1*float("Inf")
      
      a = max(first,second)
      if ((n+m) %2 ) = 1:
        return float(a)
      if l < n:
        first = A[l]
      else:
        first = float("Inf")
      if k-l+1<m:
        second = B[k-l+1]
      else:
        second = float("Inf")
      b = min(first,second)
      return (a+b) / 2.0

def main():
    s = Solution()
    c = ["a"]
    w = "a"
    print s.exist(c,w)    
  
if __name__ == "__main__":
    main()