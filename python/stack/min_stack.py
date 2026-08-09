class MinStack:
    def __init__(self): self.stack, self.minimums = [], []

    def push(self, value: int) -> None:
        self.stack.append(value); self.minimums.append(min(value, self.minimums[-1]) if self.minimums else value)

    def pop(self) -> None:
        if self.stack: self.stack.pop(); self.minimums.pop()

    def top(self) -> int:
        if not self.stack: raise IndexError("stack is empty")
        return self.stack[-1]

    def get_min(self) -> int:
        if not self.minimums: raise IndexError("stack is empty")
        return self.minimums[-1]
