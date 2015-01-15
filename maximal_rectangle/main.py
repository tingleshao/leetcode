class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if matrix == []:
          return 0
        matHist = [[0 for i in xrange(len(matrix[j]))] for j in xrange(len(matrix))]
        
        for i in xrange(len(matrix)):
          for j in xrange(len(matrix[i])):
            if matrix[i][j] == "1":
              k = i-1
              matHist[i][j] = 1
              while k >= 0:
                if matrix[i][j] == "0":
                  break
                matHist[i][j] += 1
                k-=1
   #     print matHist
        maxs = []
        for row in matHist:
          maxs.append(self.largestRectangleArea(row))
     #   print self.largestRectangleArea([1])
        
        return max(maxs)

    def largestRectangleArea(self, height):
   #     if len(height ) == 0:
  #        return 0
        stack = []
        mxArea = 0
        height.append(0)
        i = 0
        llen = len(height)
        while i < llen:
           if stack == [] or height[i] >= height[stack[0]]:
             stack.insert(0,i)             
           else:
              top = stack.pop(0)
              if stack == []:
                hh = i
              else:
                hh = i - stack[0] - 1
              area = height[top] * hh
              mxArea = max(mxArea, area)
              i-=1
           i+=1

        return mxArea
            
       
      
			
def main():
    s = Solution()
    print s.maximalRectangle("1")
 
  
if __name__ == "__main__":
    main()
             