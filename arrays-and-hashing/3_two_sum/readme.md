# Two Sum (LeetCode Q:1)

The task is to find two indices in an array such that their values add up to a given target.

---

## Approaches Summary

### 1. Brute Force

- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **Pros:** Very simple to implement. No extra memory needed.
- **Cons:** Extremely slow for large arrays because of nested loops.

---

### 2. Hash Map

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Pros:** Efficient single-pass solution. Works well even for large arrays.
- **Cons:** Requires extra memory to store the hash map. Slightly more complex than brute force.

---

## Recommendation

- Use the **hash map approach** for optimal performance in most cases since it offers linear time complexity.
- The **brute force approach** is only suitable for learning or very small input sizes.
