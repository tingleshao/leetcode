class Solution:
    # @return an integer
    def atoi(self, strr):
      while strr != "" and strr[0] == " ":
          strr = strr[1:]
      if strr == "":
        return 0
      if strr[0] not in "-+0123456789":
        return 0
      sign = 1
      if (strr[0] == "-" or strr[0] == "+") and len(strr) > 1:
        if strr[0] == "-":
          sign = -1
        strr = strr[1:]
      elif strr[0] == "-" or strr[0] == "+":        
        return 0
      num = 0
      while strr != "" and strr[0] in "0123456789":
        num = num*10
        num = num + int(strr[0])
   #     print num
        strr = strr[1:]
      num = num * sign
      if num > 2147483647:
        num = 2147483647
      if num < -2147483648:
        num = -2147483648
      return num
      
      
        


def main():  
    s = Solution()
    print s.atoi("123")
    print s.atoi("+1")
    print s.atoi("010")
    print s.atoi("2147483648")
    print s.atoi("-123")


if __name__ == "__main__":
    main()