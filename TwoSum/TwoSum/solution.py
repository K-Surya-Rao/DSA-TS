# ==================== BRUTE FORCE SOLUTION ====================
# Time Complexity: O(n²) - nested loops
# Space Complexity: O(1) - excluding output array
def two_sum_brute(nums, target):
    # Initialize result to store indices
    result = []
    
    # Outer loop: iterate through each element with index i
    for i in range(len(nums)):
        
        # Inner loop: iterate through elements after i (j > i to avoid duplicates)
        for j in range(i + 1, len(nums)):
            
            # Check if the sum of nums[i] and nums[j] equals target
            if nums[i] + nums[j] == target:
                result.append([i, j])
    
    # Return all valid pairs (LeetCode expects first pair only)
    return result[0] if result else []


# ==================== OPTIMAL SOLUTION ====================
# Time Complexity: O(n) - single pass through array
# Space Complexity: O(n) - hash map to store seen values
def two_sum_optimal(nums, target):
    # Hash map to store value -> index mapping
    seen = {}
    
    # Iterate through array once
    for i in range(len(nums)):
        # Calculate the complement needed to reach target
        complement = target - nums[i]
        
        # Check if complement exists in hash map
        if complement in seen:
            # Return indices: complement's index and current index
            return [seen[complement], i]
        
        # Store current value and its index in hash map
        seen[nums[i]] = i

        [2, 7, 11, 15]
        {
            2: 0,
            7: 1,
            11: 2,
            15: 3
        }



    
    # Return empty array if no solution found
    return []


# ==================== TEST CASES ====================
print("=== BRUTE FORCE SOLUTION ===")
print(two_sum_brute([2, 7, 11, 15], 9))      # [[0, 1]]
print(two_sum_brute([3, 2, 4], 6))           # [[1, 2]]
print(two_sum_brute([3, 3], 6))              # [[0, 1]]
print(two_sum_brute([1, 5, 3, 7, 9], 10))    # [[0, 4], [1, 2]]

print("\n=== OPTIMAL SOLUTION ===")
print(two_sum_optimal([2, 7, 11, 15], 9))    # [0, 1]
print(two_sum_optimal([3, 2, 4], 6))         # [1, 2]
print(two_sum_optimal([3, 3], 6))            # [0, 1]
print(two_sum_optimal([1, 5, 3, 7, 9], 10))  # [0, 4]