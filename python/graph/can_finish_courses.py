class CourseSchedule:
    def can_finish(self, num_courses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(num_courses)]
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)
        state = [0] * num_courses
        def cyclic(course: int) -> bool:
            if state[course]: return state[course] == 1
            state[course] = 1
            if any(cyclic(item) for item in graph[course]): return True
            state[course] = 2
            return False
        return not any(cyclic(course) for course in range(num_courses))
