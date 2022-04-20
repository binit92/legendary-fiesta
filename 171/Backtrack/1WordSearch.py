# https://leetcode.com/problems/word-search/

# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# O(n * m * 3^ w) time | O(w) space
# where n = rows in board, m = columns in board and w is length of word
# 1 approach 
def word_search(board, word):
    ROWS = len(board)
    COLS = len(board[0])
    path = set()

    def dfs(r, c, i):
        if i == len(word):
            return True
        
        if (r < 0 
            or c < 0 
            or r >= ROWS 
            or c >= COLS
            or word[i] != board[r][c]):
            return False

        ret = False
        board[r][c] = "#"

        # recursion
        ret = (dfs(r+1, c, i+1) or
                dfs(r-1, c, i+1) or
                dfs(r, c+1, i+1) or
                dfs(r, c-1, i+1))
        
        board[r][c] = word[i]
        return ret

    for r in range(ROWS):
        for c in range(COLS):
            if dfs(r,c,0):
                return True
    return False

if __name__ == '__main__':
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"    # true

    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCB"  # false
    print(word_search(board,word))