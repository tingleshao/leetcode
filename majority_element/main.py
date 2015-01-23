
class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        size = len(num)
        half_size = size / 2
        table = {}
        for i in num:
          if table.has_key(i):
            table[i] += 1
            
            if table[i] > half_size:
              
              return i
          else:
            table[i] = 1
            if table[i] > half_size:
              
              return i
          
         # print table[i]
          
        
        
        
        


        
def main():
  s = Solution()
  h = [1]
  print s.majorityElement(h)
     
if __name__ == "__main__":
    main()
    