# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def __init__(self, value=None):
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

    def add(self, elem) -> None:
        if self._list is None:
            self._list = []
            self._integer = None
        self._list.append(elem)

    def getList(self):
        return self._list

    def to_native(self):
        """Helper to convert the NestedInteger structure to native Python primitives."""
        if self.isInteger():
            return self.getInteger()
        items = self.getList()
        return [child.to_native() for child in items] if items is not None else []

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        # Edge Case: Single standalone integer (no outer brackets)
        if not s.startswith('['):
            return NestedInteger(int(s))
        
        stack = []
        num_str = []
        
        for char in s:
            if char == '[':
                # Initialize new nested list boundary
                new_list = NestedInteger()
                stack.append(new_list)
            elif char.isdigit() or char == '-':
                # Accumulate multi-character integers (including negative sign)
                num_str.append(char)
            elif char in (',', ']'):
                # Flush accumulated integer buffer into current list frame
                if num_str:
                    val = int("".join(num_str))
                    stack[-1].add(NestedInteger(val))
                    num_str.clear()
                
                # Close list boundary if closing bracket
                if char == ']' and len(stack) > 1:
                    completed_list = stack.pop()
                    stack[-1].add(completed_list)
                    
        return stack[0]


import unittest


class TestMiniParser(unittest.TestCase):
    def setUp(self):
        self.solver = Solution()

    # --- Functional & Structural Conformance ---

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

    # --- Boundary Values & Security Edge Cases ---

    def test_negative_integers_within_nested_arrays(self):
        raw = "[-1,-22,[-333,44]]"
        result = self.solver.deserialize(raw)
        self.assertEqual(result.to_native(), [-1, -22, [-333, 44]])

    def test_zero_handling(self):
        raw = "[0,[-0,0]]"
        result = self.solver.deserialize(raw)
        self.assertEqual(result.to_native(), [0, [0, 0]])

    def test_deeply_nested_recursion_simulation(self):
        """Simulates adversarial nested framing to verify stack stability."""
        depth = 50
        raw = ("[" * depth) + "101" + ("]" * depth)
        result = self.solver.deserialize(raw)
        
        # Verify unrolling
        expected = 101
        for _ in range(depth):
            expected = [expected]
        self.assertEqual(result.to_native(), expected)


if __name__ == "__main__":
    unittest.main()