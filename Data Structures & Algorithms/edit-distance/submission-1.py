class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}
        
        def dfs(i, j):
            # delete all from word1 if word2 end reached
            if j == len(word2):
                return len(word1) - i
            
            # insert remaining from word2 to word1 if word1 end reached
            if i == len(word1):
                return len(word2) - j

            if (i, j) in cache:
                return cache[(i, j)]

            if word1[i] == word2[j]:
                cache[(i, j)] = dfs(i + 1, j + 1)
            else:
                # if no match then min of all operations
                insert_op = dfs(i, j + 1)
                delete_op = dfs(i + 1, j)
                replace_op = dfs(i + 1, j + 1)

                cache[(i, j)] = 1 + min(insert_op, delete_op, replace_op)
            return cache[(i, j)]
        
        return dfs(0, 0)