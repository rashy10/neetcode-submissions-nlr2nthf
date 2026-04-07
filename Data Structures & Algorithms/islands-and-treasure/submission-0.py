class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        row , col = len(grid) , len(grid[0])
        q = deque()
        visit = set()
        

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))
        dist =0
        def addRoom(r,c):
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == -1 or (r,c) in visit:
                return 
            visit.add((r,c))
            q.append([r,c])

        while q:
            for i in range(len(q)):
                r,c = q.popleft()

                grid[r][c] = dist
                addRoom(r+1,c)
                addRoom(r-1,c)
                addRoom(r,c-1)
                addRoom(r,c+1)

            dist += 1



        