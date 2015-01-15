
class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        key_dict = {}
        key_dict['2'] = ["a","b","c"]
        key_dict['3'] = ["d","e","f"]
        key_dict['4'] = ["g","h","i"]
        key_dict['5'] = ["j","k","l"]
        key_dict['6'] = ["m","n","o"]
        key_dict['7'] = ["p","q","r","s"]
        key_dict['8'] = ["t","u","v"]
        key_dict['9'] = ["w","x","y","z"]
        key_dict['+'] = ["a","b","c"]
        key_dict['0'] = [" "]
        available = "234567890*"
        res = []
        lts = []
        if digits == "":
          return [""]
        for i in digits:
          lts.append(key_dict[i])
        code = []
        for i in xrange(len(lts)):
          code.append(0)
        st = ""
        
        while True:
          
          for i in xrange(len(lts)):
            st = st + lts[i][code[i]]
            if i == len(lts) - 1:
              res.append(st)
              
              j = i
              while j >= 0:
                if code[j] < len(lts[j]) -1:
                  code[j] += 1
                  break
                else:
                  code[j] = 0
                  j -=1
              if j == -1:
                return res
              st = ""
            
            
        


def main():
  digit = "23"
  digit2 = ""
  s = Solution()
  print s.letterCombinations(digit2)

if __name__ == "__main__":
    main()
                