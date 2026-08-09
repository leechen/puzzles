class CarFleet:
    def car_fleet(self, target: int, positions: list[int], speeds: list[int]) -> int:
        fleets: list[float] = []
        for position, speed in sorted(zip(positions, speeds), reverse=True):
            arrival = (target - position) / speed
            if not fleets or arrival > fleets[-1]:
                fleets.append(arrival)
        return len(fleets)
