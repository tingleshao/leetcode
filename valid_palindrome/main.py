class Solution:
    # @param s, a string
    # @return a boolean
    
    def isPalindrome(self, s):
        if s == "":
          return True
        i = 0
        j = len(s) -1
        while i < j:
          if s[i].lower() in "abcdefghijklmnopqrstuvwxyz1234567890" and s[j].lower() in "abcdefghijklmnopqrstuvwxyz1234567890":
            if s[i].lower() != s[j].lower():
         #     print s[i]
        #      print s[j]
              return False
            i+= 1
            j-= 1
          else:
            if s[i].lower() not in "abcdefghijklmnopqrstuvwxyz1234567890":
              i +=1
            if s[j].lower() not in "abcdefghijklmnopqrstuvwxyz1234567890":
              j -=1

        return True
              



def main():
  s = Solution()
  s1 = "A man, a plan, a canal: Panama" 
  s2 = "race a car" 
  print s.isPalindrome(s1)
  print s.isPalindrome(s2)



if __name__ == "__main__":
    main()