from collections import defaultdict
from math import floor


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
        num_dict[num].appright(i)

    for num, index in num_dict.items():
        # for cases where (target - num) == num
        if num*2 == target:
            if len(index) > 1:
                return index[:2]
        elif (target - num) in num_dict:
            return index[0], num_dict[target - num][0]

    # Sort then Binary search
    # Time: O(nlog(n))  Space: O(k) recursive or O(1) iterative
    for i, num in enumerate(nums):
        other_num = target - num
        other_num_idx = binary_search(
            nums, i+1, len(nums)-1, other_num, ordered=False)

        if other_num_idx:
            return i, other_num_idx

    return None


def binary_search_recursive(arr, left, right, target):
    # Time: O(nlogn)    Space: O(k levels deep)
    '''uses recursive binary search to locate a target number'''
    while left <= right:
        mid_idx = floor((right + left)/2)
        mid_val = arr[mid_idx]

        if mid_val == target:
            return mid_idx

        elif mid_val > target:
            # search left
            binary_search(arr, left, mid_idx-1, target)

        else:
            # search right
            binary_search(arr, mid_idx+1, right, target)
    return -1


def binary_search_iterative(arr, target):
    # Time: O(nlogn)    Space: O(1)
    '''uses iterative binary search to find a target'''
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = floor((left + right) / 2)
        if arr[middle] < target:
            left = middle + 1
        elif arr[middle] > target:
            right = middle - 1
        else:
            return middle
    return -1
