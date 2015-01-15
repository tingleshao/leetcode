class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLongestSubstringTwoDistinct(self, s):
        if not s or s == "":
            return 0
        currMax = 1
        offset = 0
        c1 = ""
        c2 = ""
        for i in xrange(len(s)):
            subs = ""

            c1 = ""
            c2 = ""
            for j in xrange(i+1,len(s)+1):
                subs+=s[j-1]
                if c1 == "":
                    c1 = c2 = s[j-1]
                elif c2 == c1:
                        c2 = s[j-1]
                else:
                    if s[j-1]!=c2 and s[j-1] != c1:
                        break
                if len(subs) > currMax:
                    currMax = len(subs)
        return currMax
                    


def main():
    s = Solution()
    print s.lengthOfLongestSubstringTwoDistinct("eceba")   
  
if __name__ == "__main__":
    main()