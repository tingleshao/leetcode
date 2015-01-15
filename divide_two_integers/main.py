class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        a = abs(dividend)
        b = abs(divisor)
        ans = 0
        i = 0
        while a>b:
          i+=1
          b = b<<1
        while i>=0:
          if a>=b:
            a-=b
            ans+=(1<<i)
          b = b>>1
          i-=1
        if( dividend > 0 and divisor > 0 ) or (dividend <0 and divisor<0):
          return ans
        return -ans


def main():
    s = Solution()
    a = 100
    b = 25
    print s.divide(a,b)    
  
if __name__ == "__main__":
    main()