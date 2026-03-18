# Detect Cycle in a Linked List — Floyd's Algorithm

> Detect if a linked list has a cycle using **two pointers** (tortoise and hare). &nbsp;⏱ Time `O(n)` &nbsp;💾 Space `O(1)`

## 🧠 The Idea

Use two pointers: `slow` moves 1 step at a time, `fast` moves 2 steps. If there's a cycle, the fast pointer will eventually **lap** the slow pointer and they'll meet. If there's no cycle, fast reaches `None` first.

```
Algorithm:
  slow, fast = head, head
  while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast: return True  ← they met → cycle!
  return False
```

## 📊 Visual

```
No cycle:     A → B → C → D → None
  fast hits None → return False

With cycle:   A → B → C
                       ↑   ↓
                       D ← E

  Step 1: slow=B, fast=C
  Step 2: slow=C, fast=E
  Step 3: slow=D, fast=D  ← MEET! → cycle detected ✓
```

## 📜 History & Background

Known as **Floyd's cycle detection algorithm**, published by **Robert W. Floyd** in 1967. Also called the "tortoise and hare" algorithm. It's used in cryptography (Pollard's rho algorithm for integer factorisation) and random number generator cycle detection.

## 💼 Tech Interview Tips

- O(1) space is the key advantage over the hash set approach (which is O(n))
- The fast pointer must check `fast` AND `fast.next` before advancing
- **Finding the cycle entry point**: after detection, reset one pointer to head, advance both 1 step at a time — they meet at the entry node
- Works for any iterable sequence, not just linked lists
- Follow-up: what's the cycle length? After meeting, keep one fixed and count steps until they meet again

## 🎯 Common Use Cases

- Linked list cycle detection (LeetCode 141, 142)
- Detecting loops in iterators / generators
- Cryptographic applications (Pollard's rho)
- Memory leak detection in reference-counted systems
- Detecting infinite loops in state machines

## 🔗 Related Problems

- [Detect Cycle](../detect_cycle/) — cycle detection in general graphs
- [Reverse Linked List](../reverse_linked_list/) — another classic linked list problem
- [Rotate Linked List](../rotate_linked_list/) — linked list manipulation
- [Merge K Lists](../merge_k_lists/) — linked list merging
