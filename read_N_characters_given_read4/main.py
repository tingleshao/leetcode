# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution:
    # @param buf, Destination buffer (a list of characters)
    # @param n,   Maximum number of characters to read (an integer)
    # @return     The number of characters read (an integer)
    def read(self, buf, n):
        if !buf:
          return None
        res = 0
        while True:
          it = read4(buf)
          if it < 4:
            res += it
            return min(res,n)
          res += 4 
          if res >= n:
            return n 
          
         
        