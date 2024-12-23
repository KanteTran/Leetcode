class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, col = len(heights), len(heights[0])
        minHeap = [[0,0,0]]
        visit = set()

        while minHeap:
            diff, r ,c = heapq.heappop(minHeap)

            if (r,c) in visit:
                continue

            visit.add((r,c))
            if (r,c) == (rows-1, col-1):
                return diff

            for i, j in [(-1,0), (1,0), (0,1), (0,-1)]:
                newR, newC = r+i, c +j
                if (newR < 0  or newC < 0 or newR == rows
                or newC == col or (newR,newC )in visit):
                    continue
                newDiff = max(diff , abs(heights[r][c] - heights[newR][newC]))
                heapq.heappush(minHeap, [newDiff, newR, newC])
