
// Definition for singly-linked list.
public class ListNode
{
    public int val;
    public ListNode next;
    public ListNode(int x) { val = x; }
}

public class ReorderListSolution
{
    public void ReorderList(ListNode head)
    {
        if (head == null || head.next == null) return;

        // Find the middle of the list using slow and fast pointer
        ListNode slow = head, fast = head.next;
        while (fast != null && fast.next != null)
        {
            slow = slow.next;
            fast = fast.next.next;
        }

        // Reverse the second half of the list
        ListNode second = slow.next;
        ListNode prev = null;
        slow.next = null;
        while (second != null)
        {
            ListNode tmp = second.next;
            second.next = prev;
            prev = second;
            second = tmp;
        }

        // Merge the two halves
        ListNode first = head;
        second = prev;
        while (second != null)
        {
            ListNode tmp1 = first.next;
            ListNode tmp2 = second.next;
            first.next = second;
            second.next = tmp1;
            first = tmp1;
            second = tmp2;
        }
    }
}
