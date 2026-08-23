class Solution:

    # Recursive solution without memoization
    def climb_stairs1(self, n: int) -> int:
        if n <= 2:
            return n

        return self.climb_stairs1(n-1) + self.climb_stairs1(n-2)

    # Recursive solution with memoization using a dictionary
    def climbStairs(self, n: int) -> int:
        memo = {}

        def climb(step: int) -> int:
            # Base cases
            if step <= 2:
                return step
            
            # Check if result is already cached
            if step in memo:
                return memo[step]
            
            # Compute and store in memo dictionary
            memo[step] = climb(step - 1) + climb(step - 2)
            return memo[step]

        return climb(n)

    # More efficient version using a list for memoization
    def climb_stairs(self, n: int) -> int:
        memo = [0] * (n + 1)

        def climb(step):
            if step <= 2: return step
            if memo[step] != 0: return memo[step]

            memo[step] = climb(step-1) + climb(step-2)
            return memo[step]

        return climb(n)