# Reverse a Linked List

> Reverse the direction of all pointers in a singly linked list **in-place**. &nbsp;⏱ Time `O(n)` &nbsp;💾 Space `O(1)`

## 🧠 The Idea

Use three pointers: `prev`, `curr`, and `next`. For each node, save the next pointer, reverse the current pointer to point backwards, then advance all three pointers forward. When `curr` is None, `prev` is the new head.

```
Algorithm:
  prev, curr = None, head
  while curr:
      next = curr.next    ← save before overwriting
      curr.next = prev    ← reverse the pointer
      prev = curr         ← advance prev
      curr = next         ← advance curr
  return prev             ← new head
```

## 📊 Visual

```
Original:   A → B → C → D → None

Step 1 (curr=A): save B, A.next=None,  prev=A, curr=B
  None ← A   B → C → D → None

Step 2 (curr=B): save C, B.next=A,     prev=B, curr=C
  None ← A ← B   C → D → None

Step 3 (curr=C): save D, C.next=B,     prev=C, curr=D
  None ← A ← B ← C   D → None

Step 4 (curr=D): save None, D.next=C,  prev=D, curr=None
  None ← A ← B ← C ← D

Return prev=D → new head!  D → C → B → A → None ✓
```

## 📜 History & Background

Linked list reversal is one of the most iconic interview problems. It appears in nearly every data structures curriculum and is often the first "pointer manipulation" problem taught. The iterative O(1) space solution is a classic test of pointer fluency.

## 💼 Tech Interview Tips

- **Iterative** (shown above): O(1) space — preferred in interviews
- **Recursive**: O(n) stack space — elegant but risk of stack overflow
- Always save `curr.next` BEFORE overwriting `curr.next`
- To **reverse a portion** (LeetCode 92): find the sublist boundaries, reverse, then reconnect
- Follow-ups: reverse in groups of K (LeetCode 25), check if list is palindrome (reverse second half)

## 🎯 Common Use Cases

- Undo/redo operations (reverse action history)
- Browser back navigation
- Text editor cursor movement
- Transaction rollback sequences

## 🔗 Related Problems

- [Detect Cycle Linked List](../detect_cycle_linked_list/) — Floyd's algorithm
- [Rotate Linked List](../rotate_linked_list/) — rotate by K positions
- [Merge K Lists](../merge_k_lists/) — linked list merging
