import pytest

from python.minStack import MinStack


def test_min_stack_tracks_minimum_across_state_changes():
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    assert stack.getMin() == -3
    stack.pop()
    assert stack.top() == 0
    assert stack.getMin() == -2


def test_min_stack_handles_duplicate_minimums():
    stack = MinStack()
    stack.push(1)
    stack.push(1)
    stack.pop()
    assert stack.getMin() == 1


@pytest.mark.parametrize("operation", ["pop", "top", "getMin"])
def test_empty_min_stack_raises_index_error(operation):
    with pytest.raises(IndexError):
        getattr(MinStack(), operation)()
