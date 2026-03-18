# Recursive Dependency Resolution

> Resolve and order task dependencies using **post-order DFS** (dependencies come before the task). &nbsp;⏱ Time `O(V+E)` &nbsp;💾 Space `O(V)`

## 🧠 The Idea

Model tasks as a graph where each task lists its dependencies. Run DFS: recursively resolve all dependencies before adding the current task to the output. Post-order traversal naturally produces a dependency-first order.

```
Algorithm:
  def dfs(task):
      name, deps = task
      for dep in deps:
          dfs(dep)          ← resolve dependencies first
      if name not in output:
          output.append(name)  ← then add this task

Result: tasks in dependency-first order (topological order)
```

## 📊 Visual

```
Task dependencies:
  A (no deps)
  B depends on A
  C depends on A, B
  D depends on A, B, C

DFS(C):
  → DFS(A): A has no deps → output: [A]
  → DFS(B):
      → DFS(A): already in output → skip
      → output: [A, B]
  → output: [A, B, C]

DFS(D) → [A, B, C, D] ✓
```

## 📜 History & Background

This pattern is essentially **topological sort** via DFS, the algorithm underlying every build system and package manager. `make` (1976), `npm`, `pip`, `gradle`, and `cargo` all use variants of this to determine the correct build/install order.

## 💼 Tech Interview Tips

- This is topological sort with memoisation — the `if name not in output` guard prevents duplicate processing
- Post-order DFS = "finish all dependencies before yourself"
- For **circular dependencies** (cycles), this will infinite-loop — add cycle detection with a "in-progress" set
- The duplicate guard means each task is added at most once, even if depended on by many tasks
- Recognise this pattern when you see: "build X before Y", "install A before B"

## 🎯 Common Use Cases

- Build systems (Makefile, CMake, Gradle, Bazel)
- Package managers (npm install, pip install, cargo build)
- CI/CD pipeline stage ordering
- Database migration ordering
- Module loading order in bundlers (webpack, rollup)

## 🔗 Related Problems

- [Topological Sort](../topo_sort/) — canonical topological sort algorithm
- [Detect Cycle](../detect_cycle/) — circular dependency detection
- [DFS](../dfs/) — the underlying traversal
