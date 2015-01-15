class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
      for i in xrange(len(board)):
        s = board[i]
        for j in xrange(len(s)):
          if board[i][j] == board[0]:
            visited = [[False for m in range(len(board[0]))] for n in range(len(board))]
            if self.DFS(board,word,visited,0,i,j):
              return True
      return False
      
    def DFS(self,board,word,visited,index,i,j):
      if i >= 0 and j >= 0 and i < len(board) and j < len(board[0]) and board[i][j] == word[index] and visited[i][j] == False:
        visited[i][j] = True
        if index + 1 == len(word):
          return True
        if self.DFS(board,word,visited,index+1,i+1,j):
          return True
        elif self.DFS(board,word,visited,index+1,i-1,j):
          return True
        elif self.DFS(board,word,visited,index+1,i,j+1):
          return True
        elif self.DFS(board,word,visited,index+1,i,j-1):
          return True
        visited[i][j] = False
      return False
        
				

def main():
    s = Solution()
    c = ["a"]
    w = "a"
    print s.exist(c,w)
    
    
    
  
if __name__ == "__main__":
    main()