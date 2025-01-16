class Solution:
    UNGUARED = 0
    GUARED = 1
    GUARD = 2
    WALL = 3

    def _mark_guared(self, row, col, grid):
        for r in range(row - 1, -1, -1):
            if grid[r][col] == self.WALL or grid[r][col] == self.GUARD:
                break
            grid[r][col] = self.GUARED

        for r in range(row + 1, len(grid)):
            if grid[r][col] == self.WALL or grid[r][col] == self.GUARD:
                break
            grid[r][col] = self.GUARED

        for c in range(col - 1, -1, -1):
            if grid[row][c] == self.WALL or grid[row][c] == self.GUARD:
                break
            grid[row][c] = self.GUARED

        for c in range(col + 1, len(grid[0])):
            if grid[row][c] == self.WALL or grid[row][c] == self.GUARD:
                break
            grid[row][c] = self.GUARED

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[self.UNGUARED] * n for _ in range(m)]
        for x, y in guards:
            grid[x][y] = self.GUARD

        for x, y in walls:
            grid[x][y] = self.WALL

        print(grid)
        for x, y in guards:
            self._mark_guared(x, y, grid)

        res = 0
        for row in grid:
            for cell in row:
                if cell == self.UNGUARED:
                    res += 1
            print(row)

        return res
