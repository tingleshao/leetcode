class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        longest = ""
        llen = len(longest)
        if s == "":
          return 0
        start = 0
        end = 0
        currlong = ""
        while end < len(s):
          if s[end] not in currlong:
            currlong = currlong + s[end]
       #     print currlong
            
          else:
     #       print "==oh"
            while start <= end:
              curr = s[start:end]
       #       print "curr: "+curr+" end: " + str(end)
              
              if s[end] not in curr:
                currlong = curr
                end-=1
                break
              start += 1
              
          if len(currlong) > len(longest):
            longest = currlong
          
          end+=1
          
     #   print longest
        return len(longest)
            
          
				

def main():
  s = Solution()
  a1 = "abcabcbb"
  a2 = "bbbbbbb"
  a3 = "hnwnkuewhsqmgbbuqcljjivswmdkqtbxixmvtrrbljptnsnfwzqfjmafadrrwsofsbcnuvqhffbsaqxwpqcac"
  a4 = "hchzvfrkmlnozjk"
  print s.lengthOfLongestSubstring(a1)
  print s.lengthOfLongestSubstring(a2)
  print s.lengthOfLongestSubstring(a3)
  print s.lengthOfLongestSubstring(a4)
  
  

if __name__ == "__main__":
    main()
             