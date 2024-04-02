
def harrints(nums, target):
    num_to_index = {}
    for i, num in enumerate(nums):
        num_to_index[num] = i

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index and num_to_index[complement] != i:
            return [i, num_to_index[complement]]

    raise ValueError("No valid solution")

# Example usage
nums1 = [2, 7, 11, 15]
target1 = 9
print(harrints(nums1, target1))  # Output: [0, 1]

nums2 = [3, 2, 4]
target2 = 6
print(harrints(nums2, target2))  # Output: [1, 2]

nums3 = [3, 3]
target3 = 6
print(harrints(nums3, target3))  # Output: [0, 1]
