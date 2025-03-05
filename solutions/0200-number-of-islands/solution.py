class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()
        islands = 0
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            q.append((r, c))
            visit.add((r, c))
            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr in range(rows) and nc in range(cols) and grid[nr][nc] == '1' and (nr, nc) not in visit):
                        q.append((nr, nc))
                        visit.add((nr, nc))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visit:
                    islands += 1
                    bfs(r, c)
        return islands
