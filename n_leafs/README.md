# N-th Level Leaf Nodes

> Count the number of leaf nodes at a given depth level in a tree. &nbsp;⏱ Time `O(n)` &nbsp;💾 Space `O(h)`

## 🧠 The Idea

Use BFS or DFS to traverse the tree, tracking depth. Count nodes at the target level that have no children (leaves).

> ⚠️ This is a placeholder — the implementation (`n_leafs.py`) is currently a stub. The concept is straightforward: level-order BFS tracks depth naturally, DFS passes depth as a parameter.

```
DFS approach:
  def count_leafs_at_level(node, target, current=0):
      if not node: return 0
      if current == target:
          return 1 if is_leaf(node) else 0
      return sum(count_leafs_at_level(child, target, current+1)
                 for child in node.children)
```

## 📊 Visual

```
Tree:
         A         ← depth 0
        / \
       B   C       ← depth 1
      / \   \
     D   E   F     ← depth 2 (all leaves here)

Leaves at depth 2: D, E, F → count = 3
Leaves at depth 1: none (B and C have children) → count = 0
Leaves at depth 0: none → count = 0
```

## 💼 Tech Interview Tips

- BFS is natural for level-based problems — process level by level with a queue
- DFS needs an explicit depth counter passed through recursion
- Distinguish "leaf at level N" from "all leaves" (leaves can be at different depths)

## 🎯 Common Use Cases

- File system: count files at a specific directory depth
- DOM tree: count nodes at a certain nesting level
- Organisational hierarchy: count employees at a specific management level

## 🔗 Related Problems

- [Longest Leaf](../longest_leaf/) — height/depth of the tree
- [BFS](../bfs/) — level-order traversal
- [DFS](../dfs/) — depth-tracked traversal
