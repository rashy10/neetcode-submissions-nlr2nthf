class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])

        visit = set()
        count = 0

        def dfs(r,c):
            if r <0 or c<0 or r >= ROWS or c >= COLS or (r,c) in visit or grid[r][c] != "1":
                return 
            visit.add((r,c))
            return (dfs(r+1,c) or dfs(r-1,c) or dfs(r,c-1) or dfs(r,c+1))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visit:
                    dfs(r,c)
                    count += 1
        return count

        