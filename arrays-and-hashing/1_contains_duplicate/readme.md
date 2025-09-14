# Contains Duplicate Problem (leetcode Q:217)

Given an integer array, check if any value appears at least twice.

---

## Approaches

### 1. Brute Force

- **Idea:** Compare every element with every other element.
- **Time Complexity:** `O(n^2)`
- **Space Complexity:** `O(1)`

**Pros:**

- Simple to implement.
- No extra memory used.

**Cons:**

- Very slow for large arrays.
- Not practical in interviews or production.

---

### 2. Sorting

- **Idea:** Sort the array, then check consecutive elements.
- **Time Complexity:** `O(n log n)`
- **Space Complexity:** `O(1)` to `O(n)` (depends on sorting algorithm).

**Pros:**

- Faster than brute force.
- Easy to understand.

**Cons:**

- Sorting changes the input array.
- Still slower than hash-based solutions.

---

### 3. HashSet (Iterative Check)

- **Idea:** Use a set to track seen elements while iterating.
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

**Pros:**

- Very efficient.
- Works in a single pass.

**Cons:**

- Extra memory required for the set.

---

### 4. HashSet (Length Check)

- **Idea:** Convert the array to a set and compare lengths.
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

**Pros:**

- Concise one-liner.
- Easy to read.

**Cons:**

- Creates a full set even if a duplicate exists early.
- Less flexible if extra logic is needed.

---

## Recommendation

- Use **HashSet** for best performance in most cases.
- Use **Sorting** if modifying the array is acceptable and memory is limited.
- Avoid **Brute Force** except for teaching or very small inputs.
