class StockSpanner:

    def __init__(self):
        self.stock = []

    def next(self, price: int) -> int:
        self.stock.append(price)
        res = 0

        for i in range(len(self.stock) - 1, -1, -1):
            if self.stock[i] <= price:
                res += 1
            else:
                break
        
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)