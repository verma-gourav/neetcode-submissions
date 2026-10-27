class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t: t[1])

        min_heap = []  # pair of [end, num_pass]
        curr_pass = 0

        for num_pass, start, end in trips:
            while min_heap and min_heap[0][0] <= start:
                curr_pass -= min_heap[0][1]
                heapq.heappop(min_heap)
            
            curr_pass += num_pass
            if curr_pass > capacity:
                return False
            
            heapq.heappush(min_heap, [end, num_pass])
        
        return True
            

            
