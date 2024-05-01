class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse = True)
        times = []

        for p, s in cars:
            t = (target - p)/s
            if (len(times) > 0) and t <= times[-1]:
                continue
            times.append(t)
            
        return len(times)
