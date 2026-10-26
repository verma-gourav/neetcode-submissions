class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, task in enumerate(tasks):
            task.append(i)
        
        tasks.sort(key=lambda t : t[0])

        res, min_heap = [], []
        i, time = 0, tasks[0][0]

        while min_heap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(min_heap, [tasks[i][1], tasks[i][2]])
                i += 1
            
            if not min_heap:
                time = tasks[i][0]
            else:
                process_time, index = heapq.heappop(min_heap)
                time += process_time
                res.append(index)
        
        return res