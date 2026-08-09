class JumpGame:
    def can_jump(self, numbers: list[int]) -> bool:
        goal = len(numbers) - 1
        for index in range(len(numbers) - 1, -1, -1):
            if index + numbers[index] >= goal: goal = index
        return goal == 0
