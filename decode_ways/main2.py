class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        length=len(s)
        if length==0:
            return 0
        D=[0]*(length+1)
        D[-1]=1
        D[-2]=1 if int(s[-1])>=1 else 0
        for i in range(length-2,-1,-1):
            bridge=True if int(s[i:i+2])>=10 and int(s[i:i+2])<=26 else False
            bonus=D[i+2] if bridge else 0
            if int(s[i])!=0:
                D[i]=D[i+1]+bonus
            else:
                D[i]=0

        return D[0]
def main():
    s = Solution()
    print s.numDecodings("12")
    print s.numDecodings("0")
    print s.numDecodings("100")
    
    
    
if __name__ == "__main__":
    main()