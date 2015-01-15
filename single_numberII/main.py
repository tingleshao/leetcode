        
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        counts = [ 0 for i in xrange(32)]
        for i in xrange(32):
          for j in xrange(len(A)):
            if A[j] >> i & 1 == 1:
              counts[i] += 1
        for i in xrange(32):
          counts[i] %= 3
        counts.reverse()
        result = 0
        if counts[0] == 1:
          for j in xrange(1,32):
            counts[j] = 1-counts[j]
        
        for j in xrange(1,31):
          result += counts[j]
          result *= 2
          
        result+=counts[31]
        if counts[0] == 1:
          result += 1
          result *= -1
   #     print counts
        return result
        

def main():  
    s = Solution()
    A = [1,2,3,1,1,3,3]
    B = [-2,-2,1,1,-3,1,-3,-3,-4,-2]
    print s.singleNumber(A)
    print s.singleNumber(B)
    
    


if __name__ == "__main__":
    main()