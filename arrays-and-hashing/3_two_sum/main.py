class Two_Sum:
    
    # ! Time Comeplexity O(n^2)
    # * Space Complexity O(1)
    def brute_force(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]
        # returning empty array for validate return type
        return []
    
    # * Time Comeplexity O(n)
    # * Space Complexity O(n)
    def hashmap(self, nums: list[int], target: int) -> list[int]:
        diff_index = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in diff_index:
                return [diff_index[diff], i]
            diff_index[diff] = i

        # returning empty array for validate return type
        return []

