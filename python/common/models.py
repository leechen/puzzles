from dataclasses import dataclass


@dataclass(eq=False)
class TreeNode:
    val: int
    left: "TreeNode | None" = None
    right: "TreeNode | None" = None


@dataclass(eq=False)
class ListNode:
    val: int
    next: "ListNode | None" = None


@dataclass
class Interval:
    start: int
    end: int
