
# Definition for a undirected graph node
class UndirectedGraphNode:
     def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        # make graph
        nodeDict = []
        seri = ""
        if node == None:
          return None
        nodeDict.append(node.label)
        bigStack= []
        bigStack.insert(0,node)
        
        while len(bigStack) != 0:
          node = bigStack.pop(0)
          seri = seri + str(node.label)
          neig = node.neighbors
          for item in neig:
            seri = seri + ","
            seri = seri + str(item.label)
            if item.label not in nodeDict:
              nodeDict.append(item.label)
              bigStack.insert(0,item)
          seri = seri + '#'
    #    print seri
        nodeDict = {}
        currNode = UndirectedGraphNode(int(seri[0]))
        head = currNode
        neighbors = []
        i = 1
        while i < len(seri):
          
          
          if seri[i] == ',':
            i+=1
            continue
          if seri[i] == "#":
            if currNode == None:
              neighbors = []
            else:
              currNode.neighbors = neighbors
              currNode = None
              neighbors = []
          else:
            if seri[i] == "-":
              val = int(seri[i:i+2])
              i = i+1
            else:
              val = int(seri[i])
            if currNode == None:
              if not nodeDict.has_key(val):
                currNode = UndirectedGraphNode(val)
                nodeDict[val] = currNode
              else:
                currNode = nodeDict[val]
            else:
              if not nodeDict.has_key(val):
                newNode = UndirectedGraphNode(val)
                neighbors.append(newNode)
                nodeDict[val] = newNode
          i+=1
        return head
          
            
          
        




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
       