class Solution:
    # @return an integer
    def romanToInt(self, s):
        res = 0
        for j in xrange(len(s)-1,-1,-1):
          if s[j] == "I":
            if res >= 5:
              res -= 1
            else:
              res +=1
          elif s[j] == "V":
            res += 5
          elif s[j] == "X":
            if res >= 50:
              res -= 10
            else:
              res += 10
          elif s[j] == "L":
            res += 50
          elif s[j] == "C":
            if res >= 500:
              res -= 100
            else:
              res += 100
          elif s[j] == "D":
            res += 500
          elif s[j] == "M":
            res += 1000
        return res