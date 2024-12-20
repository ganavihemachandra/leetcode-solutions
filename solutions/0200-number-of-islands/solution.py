class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        path = set()
        islands = 0
        q = deque()

        def bfs(r, c):
            q.append([r, c])
            path.add((r, c))
            while q:
                r, c = q.popleft()
                directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr in range(rows) and nc in range(cols) and (nr, nc) not in path and grid[nr][nc]== '1'):
                        q.append([nr, nc])
                        path.add((nr, nc))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in path:
                    islands +=1
                    bfs(r, c)
        return islands

# TC: O(rows * cols)
# SC: O(rows * cols)
