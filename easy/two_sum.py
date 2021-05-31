from collections import defaultdict
from math import floor, ceil


def twoSum(self, nums: List[int], target: int) -> List[int]:
    '''Searches a list of numbers for two values whose sum equals a target value'''

    # Brute force
    # Time: O(n^2)    Space: 1
    for i, num in enumerate(nums):
        if (target - num) in nums[i+1:]:
            return i, nums[i+1:].index(target-num) + i + 1

    # Brute force #2 (less pythonic)
    # Time: O(n^2)    Space: 1
    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums[i+1:]):
            if num1+num2 == target:
                return i, (j+i+1)

    # Dictionary
    # Time: O(n)    Space: O(n)
    num_dict = defaultdict(list)

    for i, num in enumerate(nums):
        num_dict[num].append(i)

    for num, index in num_dict.items():
        # for cases where (target - num) == num
        if num*2 == target:
            if len(index) > 1:
                return index[:2]
        elif (target - num) in num_dict:
            return index[0], num_dict[target - num][0]

    # Sort then Binary search
    # Time: O(nlog(n))  Space: log(n)?
    for i, num in enumerate(nums):
        other_num = target - num
        other_num_idx = binary_search(
            nums, i+1, len(nums)-1, other_num, ordered=False)

        if other_num_idx:
            return i, other_num_idx

    return None


def binary_search(arr, start, end, target, ordered=True):
    '''uses binary search to locate a target number'''
    if not ordered:
        arr.sort()
        binary_search(arr, start, end, target)

    while end - start >= 1:
        mid_idx = floor((end - start)/2)
        mid_val = arr[mid_idx]

        if mid_val == target:
            return mid_idx

        if mid_val > target:
            # search left
            binary_search(arr, start, mid_idx-1, target)

        if mid_val < target:
            # search right
            binary_search(arr, mid_idx+1, end, target)

    return None
