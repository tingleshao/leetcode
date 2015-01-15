class Solution:
    # @param height, a list of integer
    # @return an integer
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
              print stack, mxArea, hh, i
              i-=1
           i+=1

        return mxArea
            
				
				
      
        			
def main():
    h = [2,1,5,6,2,3]
    h2 = [6, 2, 5, 4, 5, 1, 6]
    h3 = [1]
    s = Solution()
    print s.largestRectangleArea(h)
    print s.largestRectangleArea(h3)
    
    
  
if __name__ == "__main__":
    main()