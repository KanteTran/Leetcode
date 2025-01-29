# https://leetcode.com/problems/count-unguarded-cells-in-the-grid/
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]
        total = m * n
        blocked = len(guards) + len(walls)
        guarded = set() 

        for x, y in walls:
            grid[x][y] = 3
        for x, y in guards:
            grid[x][y] = 2

        # left, right, up, down
        d = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        
        for gx, gy in guards:
            for dx, dy in d:
                x, y = gx + dx, gy + dy
                while 0 <= x < m and 0 <= y < n and grid[x][y] not in [2, 3]:
                    if (x, y) not in guarded:
                        guarded.add((x, y))
                        grid[x][y] = 1
                    x += dx
                    y += dy

        return total - blocked - len(guarded)