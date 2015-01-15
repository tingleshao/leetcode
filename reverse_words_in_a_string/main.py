class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        sl = (s.strip().split(" "))
        res = []
        for x in xrange(len(sl)):
          r  = sl[x].strip()
          if r != "":
            res.append(r)
        res.reverse()
        return " ".join(res)

def main():  
    s = Solution()
    ss = "the sky is blue"
    sss = " "
    ssss = "   a   b "
    print s.reverseWords(ss)
    print s.reverseWords(sss)
    print s.reverseWords(ssss)
    
    
    


if __name__ == "__main__":
    main()