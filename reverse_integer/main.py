class Solution:
    # @return an integer
    def reverse(self, x):
        res = 0
        flag = 0
        if x < 0:
          x = -x
          flag = 1
        while x != 0:
          res *= 10
          res += x % 10
          x /= 10
        if flag:
          res = -res
        return res