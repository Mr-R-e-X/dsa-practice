# Valid Anagram (leetcode Q:242)

The task is to determine whether two given strings are anagrams of each other.

---

## Approaches Summary

### 1. Sorting

- **Time Complexity:** O(n log n)
- **Space Complexity:** O(n)
- **Pros:** This approach is very simple and concise. It is easy to implement and understand.
- **Cons:** It is slower because sorting is required. It also uses extra memory for the sorted arrays and modifies the order of characters.

### 2. Hash Map

- **Time Complexity:** O(n)
- **Space Complexity:** O(1), since the number of possible characters is limited (for example, 26 lowercase letters).
- **Pros:** This method works for any character set and provides clear logic. It is faster than sorting.
- **Cons:** The code is slightly longer to write, and it creates two hash maps.

### 3. Hash Table (Fixed Array of 26)

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Pros:** This is the most efficient approach in terms of both speed and memory usage when the input is limited to lowercase English letters.
- **Cons:** It only works for lowercase English letters and is not flexible for other character sets such as uppercase or Unicode.

---

## Recommendation

If the input is guaranteed to be lowercase English letters, the hash table approach using a fixed-size array is the best choice because it is both fast and memory efficient.  
If the input may include a wider range of characters, the hash map approach is preferable since it handles any character set while still maintaining linear time complexity.  
The sorting approach should only be used for simplicity or quick prototyping, but it is not optimal for large inputs.
