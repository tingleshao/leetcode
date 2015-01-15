       
class Solution:
      # @param ratings, a list of integer
      # @return an integer
      def candy(self, ratings):
        candy = [1 for n in xrange(len(ratings))]
        for i in xrange(1,len(ratings)):
          if ratings[i] > ratings[i-1]:
            candy[i] = candy[i-1]+1
        if len(ratings) >= 2:
          for i in xrange(2,len(ratings)+1):
            if ratings[-i] > ratings[-(i-1)]:
              candy[-i] = max(candy[-(i-1)] + 1, candy[-i])
        return sum(candy)
         
def main():  
    s = Solution()
    r1 = [1,5,3,1]
    r2 = [2,1]
    print s.candy(r1)
    print s.candy(r2)
    
   
if __name__ == "__main__":
    main()