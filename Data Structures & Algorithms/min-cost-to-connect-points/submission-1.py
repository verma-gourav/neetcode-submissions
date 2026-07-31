class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        res = 0
        visited = set()
        min_heap = [[0, 0]] # [cost, node]
        while len(visited) < N:
            cost, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            res += cost
            visited.add(node)
            x1, y1 = points[node]
            for neig, (x2, y2) in enumerate(points):
                if neig not in visited and node != neig:
                    neig_cost = abs(x2 - x1) + abs(y2 - y1)
                    heapq.heappush(min_heap, [neig_cost, neig])
            
        return res