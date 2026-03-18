# Rotate Linked List (Right by K)

> Move the last K nodes to the front of the linked list. &nbsp;⏱ Time `O(n)` &nbsp;💾 Space `O(1)`

## 🧠 The Idea

1. Find the **length** and the **tail** of the list.
2. Handle `k % length` (rotating by full length = no-op).
3. Make the list **circular** (tail.next = head).
4. Walk `length - k` steps from the tail to find the **new tail**.
5. Set `new_head = new_tail.next` and break the circle.

```
Algorithm:
  length = 1; tail = head
  while tail.next: tail = tail.next; length++
  k = k % length
  if k == 0: return head
  tail.next = head          ← make circular
  steps = length - k
  new_tail = tail
  for _ in range(steps): new_tail = new_tail.next
  new_head = new_tail.next
  new_tail.next = None
  return new_head
```

## 📊 Visual

```
List: 1 → 2 → 3 → 4 → 5,  k = 2

Length = 5, k % 5 = 2
Make circular: 1 → 2 → 3 → 4 → 5 → (back to 1)

New tail is at position: 5 - 2 = 3 steps from tail
Walk 3 steps from tail (5): 5→1→2→3
New tail = 3, New head = 4

Break circle: 3.next = None

Result: 4 → 5 → 1 → 2 → 3  ✓
(last 2 elements moved to front)
```

## 📜 History & Background

Linked list rotation is **LeetCode 61**. The circular-list trick avoids special-casing the reconnection and is an elegant example of how temporary modification of a data structure can simplify algorithm logic.

## 💼 Tech Interview Tips

- **Always handle k % length** — rotating by length is a no-op, and k can be larger than length
- The `length - k` formula: we want the last k nodes at the front, so the new tail is at position `length - k`
- Make the list circular temporarily — cleaner than tracking multiple pointers
- Edge cases: `head == None`, `k == 0`, single element, k is a multiple of length
- Follow-up: what if k is negative (left rotation)? `k = length - (abs(k) % length)`

## 🎯 Common Use Cases

- Circular buffer / ring buffer management
- Round-robin scheduling (rotate the queue each time slot)
- Caesar cipher key rotation
- Token ring network protocols

## 🔗 Related Problems

- [Reverse Linked List](../reverse_linked_list/) — pointer manipulation on linked lists
- [Detect Cycle Linked List](../detect_cycle_linked_list/) — cycle detection
- [Merge K Lists](../merge_k_lists/) — linked list operations
