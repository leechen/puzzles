class CourseOrder:
    def find_order(self, num_courses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = [[] for _ in range(num_courses)]
        for course, prerequisite in prerequisites: graph[prerequisite].append(course)
        state, order = [0] * num_courses, []
        def visit(course: int) -> bool:
            if state[course]: return state[course] == 2
            state[course] = 1
            for dependent in graph[course]:
                if state[dependent] == 1 or not visit(dependent): return False
            state[course] = 2; order.append(course); return True
        if not all(visit(course) for course in range(num_courses)): return []
        return order[::-1]
