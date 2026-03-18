# Topological Sort — DFS

> Order nodes of a **DAG** (Directed Acyclic Graph) so every edge goes from earlier to later. &nbsp;⏱ Time `O(V+E)` &nbsp;💾 Space `O(V)`

## 🧠 The Idea

Run DFS on every unvisited node. When all of a node's **descendants** have been processed (DFS returns), push the node onto a **stack**. Reversing the stack gives the topological order — because a node is only pushed *after* everything it depends on.

```
Algorithm:
  def dfs(node):
      visited.add(node)
      for neighbour in graph[node]:
          if neighbour not in visited:
              dfs(neighbour)
      stack.append(node)      ← post-order push

  for node in graph:
      if node not in visited:
          dfs(node)

  return reversed(stack)      ← topological order
```

## 📊 Visual

```
Graph:  C → A → D → G
        C → B → D → H
             E → F → H

DFS from C:
  C → A → D → G (push G) → H (push H) → push D → push A
            → B (visited A, go to D: visited)
            → push B → push C
  E → F → H (visited) → push F → push E

Stack (bottom→top): [G, H, D, A, B, C, F, E]
Reversed: C, E, B, F, A, D, H, G  ← valid topo order ✓
```

## 📜 History & Background

Topological sort was formalised by **Arthur Kahn** (1962, BFS-based "Kahn's algorithm") and the DFS-based approach by **Robert Tarjan** (1976). It underpins every build system, package manager, and compiler dependency analysis.

## 💼 Tech Interview Tips

- Only works on **DAGs** — check for cycles first (or detect cycle during DFS)
- Two approaches: **DFS post-order + reverse** (shown here) vs **Kahn's BFS** (in-degree based)
- Kahn's algorithm is often easier to explain: repeatedly remove nodes with in-degree 0
- Topological sort is **not unique** — multiple valid orderings can exist
- If after topo sort some nodes are unprocessed → cycle exists (Kahn's makes this explicit)

## 🎯 Common Use Cases

- Build systems (Makefile, Gradle, Bazel — compile in correct order)
- Package managers (npm, pip — install dependencies before packages)
- Course prerequisite scheduling
- Compiler symbol resolution
- Database query plan optimisation (join ordering)
- CI/CD pipeline stage ordering

## 🔗 Related Problems

- [Recursive Deps](../recursive_deps/) — dependency resolution via DFS
- [Detect Cycle](../detect_cycle/) — prerequisite: graph must be a DAG
- [DFS](../dfs/) — the underlying traversal
- [Shortest Path](../shortest_path/) — longest path in DAG uses topological sort
