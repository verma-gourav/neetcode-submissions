class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        adj = { i: [] for i in range(N) } # i : list of [cost, node]

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x2 - x1) + abs(y2 - y1)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        # Prim's
        res = 0
        visited = set()
        min_heap = [[0, 0]] # [cost, point]
        while len(visited) < N:
            cost, i = heapq.heappop(min_heap)
            if i in visited:
                continue
            res += cost
            visited.add(i)
            for neig_cost, neig in adj[i]:
                if neig not in visited:
                    heapq.heappush(min_heap, [neig_cost, neig])
            
        return res