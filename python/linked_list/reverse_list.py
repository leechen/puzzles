from python.common import ListNode


class ReverseList:
    def reverse_list(self, head: ListNode | None) -> ListNode | None:
        previous = None
        while head: following = head.next; head.next = previous; previous, head = head, following
        return previous

    def reverse_list_recursive(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next: return head
        result = self.reverse_list_recursive(head.next)
        head.next.next, head.next = head, None
        return result
