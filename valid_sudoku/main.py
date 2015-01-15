class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        # check row 
        for i in xrange(9):
          row = list(board[i])
          row.sort()
          j = 1
          while j < 9:
            if row[-j] == '.':
              break
            if row[-j] == row[-(j+1)]:
              return False
            j+=1
        # check column 
        for i in xrange(9):
          col = []
          for j in xrange(9):
            col.append(board[j][i])
          col.sort()
          print col
          j = 1
          while j < 9:
            if col[-j] == '.':
              break
            if col[-j] == col[-(j+1)]:
              return False
            j+=1
        # check 3 x 3
        for i in xrange(3):
          for j in xrange(3):
            sq = []
            x = 3 * i + 1
            y = 3 * j + 1
            sq.append(board[x][y])
            sq.append(board[x-1][y-1])
            sq.append(board[x-1][y+1])
            sq.append(board[x-1][y])
            sq.append(board[x+1][y-1])
            sq.append(board[x+1][y+1])
            sq.append(board[x+1][y])
            sq.append(board[x][y-1])
            sq.append(board[x][y+1])
            sq.sort()
            j = 1
            while j < 9:
              if sq[-j] == '.':
                break
              if sq[-j] == sq[-(j+1)]:
                return False
              j+=1
        return True
            
            
        
    
def main():
  s = Solution()
  board = [[5,3,'.','.',7,'.','.','.','.'],
           [6,'.','.',1,9,5,'.','.','.'],
           ['.',9,8,'.','.','.','.',6,'.'],
           [8,'.','.','.',6,'.','.','.',3],
           [4,'.','.',8,'.',3,'.','.',1],
           [7,'.','.','.',2,'.','.','.',6],
           ['.',6,'.','.','.','.',2,8,'.'],
           ['.','.','.',4,1,9,'.','.',5],
           ['.','.','.','.',8,'.','.',7,9]]
  board2 = [['.','.',4,'.','.','.',6,3,'.'],
            ['.','.','.','.','.','.','.','.','.'],
            [5,'.','.','.','.','.','.',9,'.'],
            ['.','.','.',5,6,'.','.','.','.'],
            [4,'.',3,'.','.','.','.','.',1],
            ['.','.','.',7,'.','.','.','.','.'],
            ['.','.','.',5,'.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.','.']]
  b3 = ["....9..9.",".........","4..89...1","4.3......",".........","...5..9..","....1.7..","...4.....",".....6..."]

  print s.isValidSudoku(b3)

     
if __name__ == "__main__":
    main()
    