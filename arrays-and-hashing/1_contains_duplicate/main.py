class Contains_Duplicate:
    
    # ! Time Complexity O(n^2)
    # * Space Complexity O(1)
    def bruteforce(self, arr: list[int])->bool:
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] == arr[j]:
                    return True
        return False
    
    # ^ Time Complexity O(nlogn)
    # ^ Space Complexity O(1) or O(n) depending on the sorting algorithms
    def sorting(self, arr: list[int])->bool:
        arr.sort()
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                return True
        return False
    
    # * Time Complexity O(n)
    # ^ Space Complexity O(n)--> because we are creating a new set
    def hashset(self, arr:list[int])-> bool:
        seen = set()
        for i in arr:
            if i in seen:
                return True
            else:
                seen.add(i)
        return False
    
    # * Time Complexity O(n)
    # ^ Space Complexity O(n)--> because we are creating a new set
    def hashset_length(self, arr: list[int])->bool:
        return len(set(arr)) < len(arr)

            