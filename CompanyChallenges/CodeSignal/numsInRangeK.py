"""
Given an array of integers nums and an integer k, 
determine whether there are two distinct indices i and j in the array where nums[i] = nums[j] and the absolute difference between i and j is less than or equal to k.
"""
def solution(nums, k):
    m = {}
    n = len(nums)

    for i in range(n):
        if nums[i] in m and i - m[nums[i]] <= k:
            #if (i - m[nums[i]]) <= k:
            return True
        else:
            m[nums[i]] = i
    return False

"""
    Note the difference in below code.
"""
def solution(nums, k):
    m = {}
    n = len(nums)
    
    for i in range(n):
        if nums[i] in m: #and i - m[nums[i]] <= k:
            if (i - m[nums[i]]) <= k:
                return True
            else:
                m[nums[i]] = i
        else:
            m[nums[i]] = i
    return False
