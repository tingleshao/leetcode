class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        al = [int(j) for j in a]
        bl = [int(j) for j in b]
        al.reverse()
        bl.reverse()
        cl = []
        curry = 0
        while al != [] and bl != []:
          sm = al[0] + bl[0]
          if sm == 2:
            if curry == 1:
              cl.append(1)
            else:
              cl.append(0)
              curry = 1
          elif sm == 1:
            if curry == 1:
              cl.append(0)
            else:
              cl.append(1)
          else:
            if curry == 1:
              cl.append(1)
              curry = 0
            else:
              cl.append(0)    
          al.pop(0)
          bl.pop(0)
        if al == []:
          for bb in bl:
            sm = bb + curry
            if sm == 0:
              cl.append(sm)
            elif sm == 1:
              cl.append(sm)
              curry = 0
            else:
              cl.append(0)
              curry = 1
        else:
          for bb in al:
            sm = bb + curry
            if sm == 0:
              cl.append(sm)
            elif sm == 1:
              cl.append(sm)
              curry = 0
            else:
              cl.append(0)
              curry = 1
        if curry == 1:
          cl.append(1)      
        cl.reverse()
        res = "".join([str(j) for j in cl])
        return res
        
          
            
def main():
  s = Solution()
  print s.addBinary("11","1")

if __name__ == "__main__":
    main()