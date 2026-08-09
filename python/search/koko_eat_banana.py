class KokoEatingBananas:
    def min_eating_speed(self, piles: list[int], hours: int) -> int:
        if not piles: return 0
        left, right = 1, max(piles)
        while left < right:
            speed = (left + right) // 2
            needed = sum((pile + speed - 1) // speed for pile in piles)
            if needed <= hours: right = speed
            else: left = speed + 1
        return left
