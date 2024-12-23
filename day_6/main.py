# https://leetcode.com/problems/path-with-minimum-effort/
"""_summary_
    Find the path with the minimum effort from the top-left corner to the bottom-right corner of the matrix.
    Solution: Dijkstra's algorithm with weight = |difference in heights| 
"""
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dist = [[math.inf for _ in range(cols)] for _ in range(rows)]
        dist[0][0] = 0
        minHeap = [(0, 0, 0)] 
        
        while minHeap:
            effort, x, y = heappop(minHeap)

            if x == rows - 1 and y == cols - 1:
                return effort
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < rows and 0 <= ny < cols:
                    new_effort = max(effort, abs(heights[x][y] - heights[nx][ny]))
                    
                    if new_effort < dist[nx][ny]:
                        dist[nx][ny] = new_effort
                        heappush(minHeap, (new_effort, nx, ny))