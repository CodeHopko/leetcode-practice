from collections import defaultdict

def twoSum(self, nums: List[int], target: int) -> List[int]:
    """Searches a list of numbers for two values whose sum equals a target value"""

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
    # Time: O(nlog(n))  Space: 1
    # nums.sort()

    # for i, num in enumerate(nums):
    #     if target - num < num

    
        