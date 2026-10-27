class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        for char, cnt in [("a", a), ("b", b), ("c", c)]:
            if cnt > 0:
                heapq.heappush(max_heap, [-cnt, char])
        
        res = []
        while max_heap:
            cnt, char = heapq.heappop(max_heap)

            if len(res) >= 2 and res[-1] == char and res[-2] == char:
                if not max_heap:
                    break
                
                next_cnt, next_char = heapq.heappop(max_heap)
                res.append(next_char)
                next_cnt += 1

                if next_cnt < 0:
                    heapq.heappush(max_heap, [next_cnt, next_char])
                
                heapq.heappush(max_heap, [cnt, char])
            else:
                res.append(char)
                cnt += 1

                if cnt < 0:
                    heapq.heappush(max_heap, [cnt, char])
        
        return "".join(res)
