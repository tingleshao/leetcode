				
# hash based solution 	
class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
  def findSubstring(self, S, L):
    n = len(L) #num words
    w = len(L[0])  #length of each word
    t = n*w    # total length

    hashsum = sum([hash(x) for x in L])
    h = [hash(S[i:i+w])*(S[i:i+w] in L) for i in xrange(len(S)-w+1)]
    return [i for i in xrange(len(S)-t+1) if sum(h[i:i+t:w])==hashsum]

def main():
    s = Solution()
    c = ["a"]
    w = "a"
    print s.exist(c,w)
    
    
    
  
if __name__ == "__main__":
    main()