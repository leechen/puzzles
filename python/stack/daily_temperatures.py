class DailyTemperatures:
    def daily_temperatures(self, temperatures: list[int]) -> list[int]:
        result, stack = [0] * len(temperatures), []
        for index, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                previous = stack.pop(); result[previous] = index - previous
            stack.append(index)
        return result
