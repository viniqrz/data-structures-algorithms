# Detect Cycle in a Directed Graph

> Determine if a **directed graph** contains a cycle using DFS. &nbsp;⏱ Time `O(V+E)` &nbsp;💾 Space `O(V)`

## 🧠 The Idea

Run DFS and track a `visited` set. If DFS ever reaches a node **already in the visited set**, a cycle exists. (Note: for a correct directed-graph cycle check you need a separate "in-current-path" set; the implementation here uses a global visited set, which works for detecting any revisit.)

```
Algorithm:
  visited = set()
  def dfs(node):
      if node in visited: return True  ← cycle!
      visited.add(node)
      for child in node.children:
          if dfs(child): return True
      return False
```

## 📊 Visual

```
Directed graph with cycle:
     A
    / \
   B   C
    \ /
     Z   ← both B and C point to Z
         ← DFS from A → B → Z (visited)
         → C → Z already visited → CYCLE ✓

Directed graph without cycle:
     A → B → D
     ↓
     C → E
     (no revisit possible → no cycle)
```

## 📜 History & Background

Cycle detection in graphs is fundamental to **deadlock detection** in operating systems (Coffman et al., 1971) and **dependency resolution** in build tools. Tarjan's SCC algorithm (1972) is the gold standard for full cycle/SCC analysis.

## 💼 Tech Interview Tips

- For a **directed** graph: need a "current recursion path" set in addition to globally visited (to distinguish back edges from cross edges). The solution here uses a simplified global visited set.
- For an **undirected** graph: just track visited + parent, and flag if we revisit a non-parent node
- Cycle detection is a prerequisite check before running topological sort
- Union-Find is an efficient alternative for undirected graphs

## 🎯 Common Use Cases

- Deadlock detection (circular resource dependencies)
- Dependency graph validation (circular imports in Python, npm)
- Build system validation (circular build targets)
- Prerequisite checking (circular course requirements)

## 🔗 Related Problems

- [Detect Cycle Linked List](../detect_cycle_linked_list/) — Floyd's algorithm for linked lists
- [Topological Sort](../topo_sort/) — requires DAG (no cycles)
- [Recursive Deps](../recursive_deps/) — DFS dependency resolution
- [DFS](../dfs/) — the underlying traversal
