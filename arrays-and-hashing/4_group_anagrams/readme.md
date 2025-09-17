# Group Anagrams (LeetCode Q:49)

The task is to group an array of strings into anagrams.

---

## Approaches Summary

### 1. Sorting Each String

- **Idea:** Sort each string alphabetically and use the sorted string as the key in a hash map.
- **Time Complexity:** O(m \* n log n), where `m` = number of strings, `n` = average length of each string.
- **Space Complexity:** O(m \* n)
- **Pros:** Very simple to implement and understand.
- **Cons:** Sorting each string makes it slower for large inputs.

---

### 2. Hash Map with Character Count (Fixed Array of 26)

- **Idea:** Count the frequency of each letter using a fixed array of length 26, then use the count (as a tuple) as the key in a hash map.
- **Time Complexity:** O(m \* n)
- **Space Complexity:** O(m \* n) for storing keys and grouped results.
- **Pros:** Faster than sorting because it avoids O(n log n). Efficient for lowercase English letters.
- **Cons:** Works only for lowercase English letters. Needs adaptation for other character sets.

---

### 3. General Hash Map (Dynamic Character Frequency)

- **Idea:** Use a dictionary to count characters dynamically, allowing support for arbitrary character sets (Unicode, uppercase, etc.).
- **Time Complexity:** O(m \* n)
- **Space Complexity:** O(m \* n)
- **Pros:** Works for any character set. Still linear in performance.
- **Cons:** Slightly more complex code and less memory efficient compared to the fixed 26-length array.

---

## Recommendation

- If inputs are guaranteed to be lowercase English letters, the **fixed array of size 26** is the best option (fast and memory efficient).
- If inputs may include mixed-case or Unicode characters, use the **dynamic hash map** approach.
- The **sorting method** is easiest to implement but not optimal for large datasets.

---
