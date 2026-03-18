# Longest Path to Leaf (Tree Height / Depth)

> Find the length of the **longest path from root to a leaf node**. &nbsp;⏱ Time `O(n)` &nbsp;💾 Space `O(h)` where h = tree height

## 🧠 The Idea

Use **post-order DFS** (process children before parent). A leaf node returns 1. An internal node returns `1 + max(children heights)`. The root's return value is the total longest path.

```
Algorithm:
  def longest_leaf(node):
      if not node or no children: return 1
      return 1 + max(longest_leaf(child) for child in node.children)
```

## 📊 Visual

```
Tree:
         A          ← depth 1
        / \
       C   Z        ← depth 2
       |   |
       D   X        ← depth 3
           |
           M        ← depth 4

Post-order computation:
  longest_leaf(D) = 1  (leaf)
  longest_leaf(C) = 1 + max(1) = 2
  longest_leaf(M) = 1  (leaf)
  longest_leaf(X) = 1 + max(1) = 2
  longest_leaf(Z) = 1 + max(2) = 3
  longest_leaf(A) = 1 + max(2, 3) = 4  ✓

Longest path: A → Z → X → M (length 4)
```

## 📜 History & Background

Tree height / depth is a foundational concept in computer science — the height of a balanced binary tree is O(log n), which determines the efficiency of BSTs, heaps, and B-trees. Post-order traversal for computing properties was systematised by Knuth in *The Art of Computer Programming* (1968).

## 💼 Tech Interview Tips

- This is essentially **tree height** — same algorithm used in AVL trees to maintain balance
- For **binary trees**: `height(node) = 1 + max(height(left), height(right))`; `None` returns 0 (or -1 for edges vs nodes)
- Distinguish: **depth** of a node = distance from root; **height** of a node = distance to deepest leaf
- Diameter of a tree (LeetCode 543): at each node, `left_height + right_height` → take global max

## 🎯 Common Use Cases

- Checking if a binary tree is balanced (|left_height - right_height| ≤ 1 at every node)
- Evaluating time complexity of tree operations
- DOM tree depth analysis (browser rendering)
- File system depth traversal

## 🔗 Related Problems

- [House Robber III](../house_robber_3/) — post-order tree DP
- [DFS](../dfs/) — the traversal used here
- [N Leafs](../n_leafs/) — counting leaf nodes
