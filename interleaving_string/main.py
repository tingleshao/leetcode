
class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
   #    print len(s1)
   #    print len(s2)
   #s    print len(s3)
       if len(s3) != (len(s1) + len(s2)):
         return False

       table = [[False for i in range(len(s2)+1)] for j in range(len(s1)+1)]
 #      print table
      
       for i in xrange(len(s1)+1):
         for j in xrange(len(s2)+1):
           if i == 0 and j == 0:
             table[i][j] = True
           elif i == 0:
     #        print "i:"+str(i) 
     #        print "j:"+str(j)
     #        print "a1"+str(s3[i+j-1]) 
     #        print "xx"
             table[i][j] = table[i][j-1] and s2[j-1] == s3[i+j-1]
           elif j == 0:
             table[i][j] = table[i-1][j] and s1[i-1] == s3[i+j-1]
           else:
             table[i][j] = (table[i-1][j] and s1[i-1] == s3[i+j-1]) or (table[i][j-1] and s2[j-1] == s3[i+j-1])
     #  print table
       return table[len(s1)][len(s2)]
       
def main():
    s = Solution()
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    s4 = "aadbbbaccc"
    print s.isInterleave(s1,s2,s3)
    print "======"
    print s.isInterleave(s1,s2,s4)
    
if __name__ == "__main__":
    main()