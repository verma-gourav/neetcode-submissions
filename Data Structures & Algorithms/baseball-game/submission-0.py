class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []
        op = ["+", "D", "C"]

        for i in range(len(operations)):
            if operations[i] not in op:
                arr.append(int(operations[i]))

            elif operations[i] == "+":
                val = arr[-1] + arr[-2]
                arr.append(val)
            
            elif operations[i] == "D":
                val = arr[-1] * 2
                arr.append(val)
            
            elif operations[i] == "C":
                arr.pop()
            
            else:
                return -1
        
        return sum(arr)