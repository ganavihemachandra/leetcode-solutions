class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if (r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in path or word[i]!= board[r][c]):
                return False
            
            path.add((r,c))
            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if dfs(nr, nc , i+1):
                    return True
            path.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
