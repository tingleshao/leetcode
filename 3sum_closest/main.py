class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
      if len(num) < 3:
        mx = 0
        for i in num:
          mx += i
          return mx 
      n = len(num)
      num.sort()
      i = 0
      ps = float('inf')
      while i < n - 2:
        j = i+1
        k = n-1
        while j < k:
          s = num[i] + num[j] + num[k]
          if abs(s-target) < abs(ps-target):
            ps = s 
          if s == target:
      #      print "ijk: " + str(i) + " " + str(j) + " " + str(k)
            return ps
      #    print "ijk: " + str(i) + " " + str(j) + " " + str(k) + " ps: " + str(ps)
          
          if s > target:
            k -= 1
          else:
            j += 1
        i+=1
     #   print "ijk: " + str(i) + " " + str(j) + " " + str(k)
      return ps
      
        
				
def main():
  s = Solution()
  print s.threeSumClosest([-1,2,1,-4],1)
  
  
  

     
if __name__ == "__main__":
    main()
           