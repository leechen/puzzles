"""Deserialize a nested-integer string using recursive descent."""

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
        result, _ = self._parse(s, 0)
        return result

    def _parse(self, s: str, index: int) -> tuple[NestedInteger, int]:
        if s[index] != "[":
            number_end = index
            if s[number_end] == "-":
                number_end += 1
            while number_end < len(s) and s[number_end].isdigit():
                number_end += 1
            return NestedInteger(int(s[index:number_end])), number_end

        result = NestedInteger()
        index += 1

        while s[index] != "]":
            child, index = self._parse(s, index)
            result.add(child)

            if s[index] == ",":
                index += 1

        return result, index + 1


class TestMiniParserRecursive(unittest.TestCase):
    def setUp(self):
        self.solver = Solution()

    def test_valid_representations(self):
        cases = {
            "324": 324,
            "-42": -42,
            "[]": [],
            "[123,456,789]": [123, 456, 789],
            "[123,[456,[789]]]": [123, [456, [789]]],
            "[[],[[]]]": [[], [[]]],
            "[-1,-22,[-333,44]]": [-1, -22, [-333, 44]],
            "[0,[-0,0]]": [0, [0, 0]],
            "[-2147483648,2147483647]": [-2147483648, 2147483647],
        }

        for raw, expected in cases.items():
            with self.subTest(raw=raw):
                self.assertEqual(self.solver.deserialize(raw).to_native(), expected)

    def test_deeply_nested_input(self):
        depth = 50
        raw = ("[" * depth) + "101" + ("]" * depth)

        expected = 101
        for _ in range(depth):
            expected = [expected]

        self.assertEqual(self.solver.deserialize(raw).to_native(), expected)


if __name__ == "__main__":
    unittest.main()
