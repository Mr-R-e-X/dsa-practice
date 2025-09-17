from collections import defaultdict

class Group_Anagrams:
    # ^ Time Complexity O(m*nlogn)
    # * Space Complexity O(n*m)
    def sorting(self, strs: list[str])-> list[list[str]]:
        keys = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            keys[sorted_s].append(s)
        return list(keys.values())
    
    # * Time Complexity O(m*n)
    # * Space Complexity O(n*m)
    def hash_table(self, strs: list[str]) -> list[list[str]]:
        keys = defaultdict(list)
        for s in strs:
            count = [0]*26
            for char in s:
                count[ord(char)-ord('a')] += 1
            keys[tuple(count)].append(s)
        return list(keys.values())
    
    # * Time Complexity O(m*n)
    # * Space Complexity O(n*m)
    def dynamic_hash(self, strs: list[str]) -> list[list[str]]:
        keys = defaultdict(list)
        for s in strs:
            freq={}
            for char in s:
                freq[char] = freq.get(char, 0)+1
            key = tuple(sorted(freq.items()))
            keys[key].append(s)
        return list(keys.values())