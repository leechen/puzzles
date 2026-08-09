class StockTrade:
    def max_profit(self, prices: list[int]) -> int:
        minimum, best = float("inf"), 0
        for price in prices: minimum = min(minimum, price); best = max(best, price - minimum)
        return best
