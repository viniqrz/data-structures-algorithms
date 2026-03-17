# Rotate Image 90° Clockwise

> Rotate an n×n matrix 90 degrees clockwise **in-place**. &nbsp;⏱ Time `O(n²)` &nbsp;💾 Space `O(1)`

## 🧠 The Idea

Two steps: **reverse the rows** (flip the matrix upside-down), then **transpose** (swap `matrix[i][j]` with `matrix[j][i]`). Together these produce a 90° clockwise rotation.

```
90° clockwise  = reverse rows + transpose
90° counter-clockwise = transpose + reverse rows
180°           = reverse rows + reverse each row
```

## 📊 Visual

```
Original:        After reverse rows:    After transpose:
1 2 3            7 8 9                  7 4 1
4 5 6    →→      4 5 6        →→        8 5 2
7 8 9            1 2 3                  9 6 3

Result (90° CW):  7 4 1
                  8 5 2
                  9 6 3   ✓

Verify: top-left corner 1 moved to top-right (correct for CW rotation ✓)
```

## 📜 History & Background

Matrix rotation is a fundamental operation in **computer graphics** and **image processing**. Rotation by 90° is special because it can be done in-place without any extra memory — a key insight used in image libraries, game engines, and display drivers.

## 💼 Tech Interview Tips

- Memorise the two approaches: (1) **reverse + transpose** for CW, (2) **transpose + reverse** for CCW
- Transpose loop: `for i in range(n): for j in range(i): swap(matrix[i][j], matrix[j][i])` — note `range(i)` to avoid double-swapping
- Only works for **square** matrices in-place; non-square requires extra space
- LeetCode 48
- Common trick: draw a small 3×3 example to verify direction before coding

## 🎯 Common Use Cases

- Image rotation (photo apps, game sprites)
- Display orientation changes (phone tilt)
- Game board manipulation (Tetris piece rotation)
- Matrix operations in graphics pipelines (OpenGL/WebGL transformations)

## 🔗 Related Problems

- [Grid Traversal](../grid_traversal/) — 2D matrix traversal
- [Dutch National Flag](../dutch_national_flag/) — in-place array manipulation
