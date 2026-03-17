# House Robber III — Tree Dynamic Programming

> Rob houses on a binary tree: **can't rob a node and its direct child**. Maximise total. &nbsp;⏱ Time `O(n)` &nbsp;💾 Space `O(h)`

## 🧠 The Idea

For each node, there are exactly two choices: **rob it** (can't rob its children) or **skip it** (children are free to rob or skip). Use post-order DFS — process children first, then decide for the current node. Return a **pair `[skip, rob]`** from each subtree.

```
dp(node) → [skip_node, rob_node]
  skip_node = max(left[0], left[1]) + max(right[0], right[1])
  rob_node  = node.val + left[0] + right[0]

Answer: max(dp(root))
```

## 📊 Visual

```
        3
       / \
      2   3
       \   \
        3   1

dp(3_left_child)  = [0, 3]  → max=3
dp(3_right_child) = [0, 1]  → max=1
dp(2) = [max(0,3) + max(0,0), 2 + 0 + 0] = [3, 2]
dp(3R)= [max(0,0) + max(0,1), 3 + 0 + 0] = [1, 3]
dp(3_root) = [max(3,2) + max(1,3), 3 + 3 + 1] = [6, 7]
Answer: max(6, 7) = 7  ✓  (rob root 3 + right child 3 + right-right 1)
```

## 📜 History & Background

**LeetCode 337** — part of the House Robber series (I: linear array, II: circular array, III: binary tree). The series elegantly demonstrates how the same DP idea scales across different graph structures.

## 💼 Tech Interview Tips

- **Post-order traversal** is the key — process children before making decisions about the parent
- Return a **pair** `[not_robbed, robbed]` from each node rather than a single value
- This avoids recomputing subtrees (otherwise exponential via naive recursion)
- The pattern `dp(node) → (skip, take)` applies to many tree DP problems
- Interviewers often ask: "why not just memoize?" — the pair approach is cleaner and avoids a separate cache

## 🎯 Common Use Cases

- Tree-structured resource allocation with adjacency constraints
- Network security (can't activate adjacent intrusion detectors simultaneously)
- Hierarchical scheduling (manager can't be in the same meeting as direct report)

## 🔗 Related Problems

- [Longest Leaf](../longest_leaf/) — another post-order tree DP
- [Knapsack](../knapsack/) — general DP with include/exclude decisions
- [DFS](../dfs/) — the traversal underlying this solution
