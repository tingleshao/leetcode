class Solution:
    # @return an integer
    def maxArea(self, height):
        maxVol = 0
        low = 0
        high = len(height) - 1
        while low < high:
          vol = (high-low ) * min([height[low],height[high]])
          if vol > maxVol:
            maxVol = vol  
          if height[low] < height[high]:
            low += 1
          else: 
            high -= 1
        return maxVol
        
        
def main():
  s = Solution()
  h = [3,2,4,4,2]
  print s.maxArea(h)
     
if __name__ == "__main__":
    main()
    