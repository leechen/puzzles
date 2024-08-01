public class ReverseListSolution
{
    public ListNode ReverseList(ListNode head)
    {
        ListNode prev = null, curr = head;

        while (curr != null)
        {
            var nxt = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nxt;
        }
        return prev;
    }
}


public class ReverseListRecursiveSolution
{
    public ListNode ReverseListRecursive(ListNode head) {
        ListNode Reverse(ListNode cur, ListNode prev) {
            if (cur == null) {
                return prev;
            } else {
                ListNode next = cur.next;
                cur.next = prev;
                return Reverse(next, cur);
            }
        }

        return Reverse(head, null);
    }
}