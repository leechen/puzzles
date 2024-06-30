using System;
using System.Collections.Generic;

public class MinStack {

    private List<int> stack;
    private List<int> min;

    /** Initialize your data structure here. */
    public MinStack() {
        stack = new List<int>();
        min = new List<int>();
    }

    public void Push(int val) {
        stack.Add(val);
        if (min.Count == 0) {
            min.Add(val);
        } else {
            min.Add(Math.Min(val, min[min.Count - 1]));
        }
    }

    public void Pop() {
        if (stack.Count > 0) {
            stack.RemoveAt(stack.Count - 1);
            min.RemoveAt(min.Count - 1);
        }
    }

    public int Top() {
        if (stack.Count > 0) {
            return stack[stack.Count - 1];
        }
        throw new InvalidOperationException("Stack is empty");
    }

    public int GetMin() {
        if (min.Count > 0) {
            return min[min.Count - 1];
        }
        throw new InvalidOperationException("Stack is empty");
    }
}

// Your MinStack object will be instantiated and called as such:
// MinStack obj = new MinStack();
// obj.Push(val);
// obj.Pop();
// int param_3 = obj.Top();
// int param_4 = obj.GetMin();
