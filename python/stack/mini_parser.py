"""Deserialize a nested-integer string without recursion."""

import unittest


class NestedInteger:
    """Local implementation of the interface supplied by LeetCode."""

    def __init__(self, value: int | None = None) -> None:
        self._integer: int | None
        self._list: list[NestedInteger] | None

        if value is not None:
            self._integer = value
            self._list = None
        else:
            self._integer = None
            self._list = []

    def isInteger(self) -> bool:
        return self._integer is not None

    def getInteger(self) -> int:
        if self._integer is None:
            raise ValueError("NestedInteger is not an integer")
        return self._integer

    def setInteger(self, value: int) -> None:
        self._integer = value
        self._list = None

    def add(self, elem: "NestedInteger") -> None:
        if self._list is None:
            self._list = []
            self._integer = None
        self._list.append(elem)

    def getList(self) -> list["NestedInteger"] | None:
        return self._list

    def to_native(self) -> int | list[object]:
        """Convert this object to native Python values for inspection and tests."""
        if self.isInteger():
            return self.getInteger()

        items = self.getList()
        return [child.to_native() for child in items] if items is not None else []


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        """Parse a valid nested-integer representation in O(n) time."""
        if not s.startswith("["):
            return NestedInteger(int(s))

        stack: list[NestedInteger] = []
        number_chars: list[str] = []

        for char in s:
            if char == "[":
                stack.append(NestedInteger())
            elif char.isdigit() or char == "-":
                number_chars.append(char)
            elif char in {",", "]"}:
                if number_chars:
                    value = int("".join(number_chars))
                    stack[-1].add(NestedInteger(value))
                    number_chars.clear()

                if char == "]" and len(stack) > 1:
                    completed = stack.pop()
                    stack[-1].add(completed)

        return stack[0]


class TestMiniParser(unittest.TestCase):
    def setUp(self):
        self.solver = Solution()

    def test_single_standalone_positive_integer(self):
        result = self.solver.deserialize("324")
        self.assertTrue(result.isInteger())
        self.assertEqual(result.getInteger(), 324)
        self.assertEqual(result.to_native(), 324)

    def test_single_standalone_negative_integer(self):
        result = self.solver.deserialize("-42")
        self.assertTrue(result.isInteger())
        self.assertEqual(result.getInteger(), -42)
        self.assertEqual(result.to_native(), -42)

    def test_flat_list_multiple_elements(self):
        raw = "[123,456,789]"
        result = self.solver.deserialize(raw)
        self.assertFalse(result.isInteger())
        self.assertEqual(result.to_native(), [123, 456, 789])

    def test_nested_hierarchical_list(self):
        raw = "[123,[456,[789]]]"
        result = self.solver.deserialize(raw)
        self.assertEqual(result.to_native(), [123, [456, [789]]])

    def test_empty_list_payload(self):
        raw = "[]"
        result = self.solver.deserialize(raw)
        self.assertFalse(result.isInteger())
        self.assertEqual(result.to_native(), [])

    def test_nested_empty_structures(self):
        raw = "[[],[[]]]"
        result = self.solver.deserialize(raw)
        self.assertEqual(result.to_native(), [[], [[]]])

    def test_negative_integers_within_nested_arrays(self):
        raw = "[-1,-22,[-333,44]]"
        result = self.solver.deserialize(raw)
        self.assertEqual(result.to_native(), [-1, -22, [-333, 44]])

    def test_zero_handling(self):
        raw = "[0,[-0,0]]"
        result = self.solver.deserialize(raw)
        self.assertEqual(result.to_native(), [0, [0, 0]])

    def test_32_bit_integer_boundaries(self):
        raw = "[-2147483648,2147483647]"
        result = self.solver.deserialize(raw)
        self.assertEqual(result.to_native(), [-2147483648, 2147483647])

    def test_deeply_nested_recursion_simulation(self):
        """Verify that parsing deeply nested input does not use recursion."""
        depth = 50
        raw = ("[" * depth) + "101" + ("]" * depth)
        result = self.solver.deserialize(raw)

        expected = 101
        for _ in range(depth):
            expected = [expected]
        self.assertEqual(result.to_native(), expected)


if __name__ == "__main__":
    unittest.main()
