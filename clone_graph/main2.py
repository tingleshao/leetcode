

# Definition for a undirected graph node
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
      if node == None:
        return None
      return self.dfs(node,{})
      
      
    def dfs(self,node,ndict):
      p = UndirectedGraphNode(node.label)
      ndict[p.label] = p
      
      for n in node.neighbors:
        if ndict.has_key(n.label):
          p.neighbors.append(ndict[n.label])
        else:
          p.neighbors.append(self.dfs(n,ndict))
      return p
        



def main():
  s = Solution()
  n0 = UndirectedGraphNode(0)
  n1 = UndirectedGraphNode(1)
  n2 = UndirectedGraphNode(2)
  n0.neighbors = [n1,n2]
  n1.neighbors = [n2]
  n2.neighbors = [n2]
  
  
  print s.cloneGraph(n0)



if __name__ == "__main__":
    main()
       