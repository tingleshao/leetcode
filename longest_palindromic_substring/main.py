class Solution:
    # @return a string
    def longestPalindrome(self, s):
       n = len(s)
       P = [[0 for i in xrange(n)] for j in xrange(n)]
       maxL = 0
       start = 0
       end = 0
       for i in xrange(n):
         for j in xrange(i):
           P[j][i] = s[j]==s[i] and (i-j < 2 or P[j+1][i-1] == 1)
           if P[j][i] == 1 and maxL < i-j+1:
             maxL = i-j+1
             start = j
             end = i
         P[i][i] = 1
         
       return s[start:end+1]    
              
def main():
    s1 = "a"
    s2 = "bb"
    s3 = "abb"
    s4 = "ccd"
    s = Solution()
    print s.longestPalindrome(s1)
    print s.longestPalindrome(s2)
    print s.longestPalindrome(s3)
    print s.longestPalindrome(s4)
    
    
    
if __name__ == "__main__":
    main()