# ==================== BRUTE FORCE SOLUTION ====================
# Time Complexity: O(n²) - creating new array and copying elements
# Space Complexity: O(n) - for the temporary result array
def removeElement_brute(nums, val):
    """
    Brute Force Approach:
    - Create a new temporary array
    - Iterate through original array and copy elements != val
    - Copy back to original array
    """
    # Create temporary array to store valid elements
    temp = []
    
    # Iterate through all elements
    for i in range(len(nums)):
        # If element is not equal to val, add to temp array
        if nums[i] != val:
            temp.append(nums[i])
    
    # Copy elements back to original array
    for i in range(len(temp)):
        nums[i] = temp[i]
    
    # Return count of valid elements
    return len(temp)


# ==================== OPTIMAL SOLUTION (Two Pointers) ====================
# Time Complexity: O(n) - single pass through array
# Space Complexity: O(1) - only using two pointers, in-place modification
def removeElement_optimal(nums, val):
    """
    Two Pointer Approach:
    - Use 'k' as slow pointer to track position for valid elements
    - Use 'i' as fast pointer to scan through array
    - When we find element != val, place it at position k and increment k
    
    Visualization for [3,2,2,3], val=3:
    
    Initial: [3, 2, 2, 3], k=0
    
    i=0: nums[0]=3 == 3, skip (k=0)
    i=1: nums[1]=2 != 3, nums[0]=2, k=1 → [2, 2, 2, 3]
    i=2: nums[2]=2 != 3, nums[1]=2, k=2 → [2, 2, 2, 3]
    i=3: nums[3]=3 == 3, skip (k=2)
    
    Result: k=2, first 2 elements are [2, 2]
    
    Visualization for [0,1,2,2,3,0,4,2], val=2:
    
    Initial: [0, 1, 2, 2, 3, 0, 4, 2], k=0
    
    i=0: nums[0]=0 != 2, nums[0]=0, k=1 → [0, 1, 2, 2, 3, 0, 4, 2]
    i=1: nums[1]=1 != 2, nums[1]=1, k=2 → [0, 1, 2, 2, 3, 0, 4, 2]
    i=2: nums[2]=2 == 2, skip (k=2)
    i=3: nums[3]=2 == 2, skip (k=2)
    i=4: nums[4]=3 != 2, nums[2]=3, k=3 → [0, 1, 3, 2, 3, 0, 4, 2]
    i=5: nums[5]=0 != 2, nums[3]=0, k=4 → [0, 1, 3, 0, 3, 0, 4, 2]
    i=6: nums[6]=4 != 2, nums[4]=4, k=5 → [0, 1, 3, 0, 4, 0, 4, 2]
    i=7: nums[7]=2 == 2, skip (k=5)
    
    Result: k=5, first 5 elements are [0, 1, 3, 0, 4]
    """
    # Initialize pointer k to track position for next valid element
    k = 0
    
    # Iterate through array with fast pointer i
    for i in range(len(nums)):
        # If current element is not equal to val, it should be kept
        if nums[i] != val:
            # Place element at position k
            nums[k] = nums[i]
            # Move k pointer forward
            k += 1
    
    # Return count of valid elements
    return k


# ==================== ALTERNATIVE OPTIMAL SOLUTION (Swap from End) ====================
# Time Complexity: O(n) - single pass through array
# Space Complexity: O(1) - in-place modification
def removeElement_swap(nums, val):
    """
    Swap Approach (Alternative):
    - When we find element == val, swap with element from end
    - Decrease array size consideration
    - Continue until we've checked all relevant positions
    - More efficient when elements to remove are rare
    
    Visualization for [3,2,2,3], val=3:
    
    Initial: [3, 2, 2, 3], i=0, n=4
    
    i=0: nums[0]=3 == 3, swap with nums[3], n=3 → [3, 2, 2, 3], i=0
    i=0: nums[0]=3 == 3, swap with nums[2], n=2 → [2, 2, 2, 3], i=0
    i=0: nums[0]=2 != 3, i=1
    i=1: nums[1]=2 != 3, i=2
    i=2: i >= n, stop
    
    Result: n=2, first 2 elements are [2, 2]
    """
    # Start from the end of array
    n = len(nums)
    i = 0
    
    while i < n:
        # If current element equals val, swap with last element
        if nums[i] == val:
            nums[i] = nums[n - 1]
            n -= 1  # Reduce the size we're considering
        else:
            i += 1  # Move to next element only if current is valid
    
    return n


# ==================== TEST CASES ====================
print("=== BRUTE FORCE SOLUTION ===")
nums1 = [3, 2, 2, 3]
k1 = removeElement_brute(nums1, 3)
print(f"Input: [3,2,2,3], val=3 → k={k1}, nums={nums1[:k1]}")  # k=2, nums=[2,2]

nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
k2 = removeElement_brute(nums2, 2)
print(f"Input: [0,1,2,2,3,0,4,2], val=2 → k={k2}, nums={nums2[:k2]}")  # k=5, nums=[0,1,3,0,4]

nums3 = [1]
k3 = removeElement_brute(nums3, 1)
print(f"Input: [1], val=1 → k={k3}, nums={nums3[:k3]}")  # k=0, nums=[]

nums4 = [4, 5]
k4 = removeElement_brute(nums4, 4)
print(f"Input: [4,5], val=4 → k={k4}, nums={nums4[:k4]}")  # k=1, nums=[5]


print("\n=== OPTIMAL SOLUTION (Two Pointers) ===")
nums5 = [3, 2, 2, 3]
k5 = removeElement_optimal(nums5, 3)
print(f"Input: [3,2,2,3], val=3 → k={k5}, nums={nums5[:k5]}")  # k=2, nums=[2,2]

nums6 = [0, 1, 2, 2, 3, 0, 4, 2]
k6 = removeElement_optimal(nums6, 2)
print(f"Input: [0,1,2,2,3,0,4,2], val=2 → k={k6}, nums={nums6[:k6]}")  # k=5

nums7 = [1]
k7 = removeElement_optimal(nums7, 1)
print(f"Input: [1], val=1 → k={k7}, nums={nums7[:k7]}")  # k=0, nums=[]

nums8 = [4, 5]
k8 = removeElement_optimal(nums8, 4)
print(f"Input: [4,5], val=4 → k={k8}, nums={nums8[:k8]}")  # k=1, nums=[5]


print("\n=== SWAP APPROACH (Alternative) ===")
nums9 = [3, 2, 2, 3]
k9 = removeElement_swap(nums9, 3)
print(f"Input: [3,2,2,3], val=3 → k={k9}, nums={nums9[:k9]}")  # k=2

nums10 = [0, 1, 2, 2, 3, 0, 4, 2]
k10 = removeElement_swap(nums10, 2)
print(f"Input: [0,1,2,2,3,0,4,2], val=2 → k={k10}, nums={nums10[:k10]}")  # k=5

nums11 = [1]
k11 = removeElement_swap(nums11, 1)
print(f"Input: [1], val=1 → k={k11}, nums={nums11[:k11]}")  # k=0

nums12 = [4, 5]
k12 = removeElement_swap(nums12, 4)
print(f"Input: [4,5], val=4 → k={k12}, nums={nums12[:k12]}")  # k=1


# ==================== COMPLEXITY COMPARISON ====================
print("\n=== COMPLEXITY ANALYSIS ===")
print("""
┌─────────────────────┬──────────────────┬──────────────────┐
│     Approach        │ Time Complexity  │ Space Complexity │
├─────────────────────┼──────────────────┼──────────────────┤
│ Brute Force         │ O(n²)            │ O(n)             │
│ Two Pointers        │ O(n)             │ O(1)             │
│ Swap from End       │ O(n)             │ O(1)             │
└─────────────────────┴──────────────────┴──────────────────┘

Best Approach: Two Pointers (Optimal)
- Single pass through array
- In-place modification (no extra space)
- Maintains relative order of kept elements
- Best for general case

Swap Approach:
- Also O(n) time and O(1) space
- More efficient when elements to remove are rare
- Does NOT maintain relative order
- Fewer writes when val is rare in array
""")


# ==================== EDGE CASES ====================
print("\n=== EDGE CASES ===")
# Empty array
nums13 = []
k13 = removeElement_optimal(nums13, 1)
print(f"Empty array: nums=[], val=1 → k={k13}")

# All elements are val
nums14 = [2, 2, 2, 2]
k14 = removeElement_optimal(nums14, 2)
print(f"All same: nums=[2,2,2,2], val=2 → k={k14}")

# No elements are val
nums15 = [1, 2, 3, 4]
k15 = removeElement_optimal(nums15, 5)
print(f"None match: nums=[1,2,3,4], val=5 → k={k15}, nums={nums15[:k15]}")

# Single element that is val
nums16 = [1]
k16 = removeElement_optimal(nums16, 1)
print(f"Single match: nums=[1], val=1 → k={k16}")

# Single element that is not val
nums17 = [1]
k17 = removeElement_optimal(nums17, 2)
print(f"Single no match: nums=[1], val=2 → k={k17}, nums={nums17[:k17]}")