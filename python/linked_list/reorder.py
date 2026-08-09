from python.common import ListNode


class ReorderList:
    def reorder_list(self, head: ListNode | None) -> None:
        if not head or not head.next: return
        slow, fast = head, head.next
        while fast and fast.next: slow, fast = slow.next, fast.next.next
        second, slow.next = slow.next, None
        previous = None
        while second: following = second.next; second.next = previous; previous, second = second, following
        first, second = head, previous
        while second:
            first_next, second_next = first.next, second.next
            first.next, second.next = second, first_next
            first, second = first_next, second_next
