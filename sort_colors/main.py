
class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
      w = -1
      b = -1
      r = -1
      for j in xrange(len(A)):
        if A[j] == 2:
          if b == -1:
            if w == -1:
              if r == -1:
                A[0] = 2
                b = 0
              else:
                A[r+1] = 2
                b = r+1
            else:
              A[w+1] = 2
              b = w+1
          else:
            A[b+1] = 2
            b+=1
        if A[j] == 1:
          if w == -1:
            if b == -1:
              if r == -1:
                A[0] = 1
                w = 0
              else:
                A[r+1] = 1
                w = r +1
            else:
              if r == -1:
                A[0] = 1
                w = 0
                A[b+1] = 2
                b = b+1
              else:
                A[r+1] = 1
                w = r+1
                A[b+1] = 2
                b = b+1
          else:
            if b == -1:
              A[w+1] = 1
              w = w+1
            else:
              A[w+1] = 1
              w = w+1
              A[b+1] = 2
              b = b+1
        if A[j] == 0:
          if r == -1:
            if b == -1:
              if w == -1:
                A[0] = 0
                r = 0
              else:
                A[0] = 0
                r = 0
                A[w+1] = 1
                w += 1
            else:
              if w == -1:
                A[0] = 0
                r = 0
                A[b+1] = 2
                b +=1
              else:
                A[0] = 0
                r = 0
                A[b+1] = 2
                b += 1
                A[w+1] = 1
                w+=1
          else:
            if b == -1:
              if w == -1:
                A[r+1] = 0
                r +=1
              else:
                A[r+1] = 0
                r+=1
                A[w+1] = 1
                w+=1
            else:
              if w == -1:
                A[r+1] = 0
                r+=1
                A[b+1] = 2
                b+=1
              else:
                A[r+1] = 0
                r+=1
                A[b+1] = 2
                b+=1
                A[w+1] = 1
                w+=1
          
                        				
def main(): 
    s = Solution()
    A = [1]
    s.sortColors(A)
    print A

if __name__ == "__main__":
    main()