"""
Given a sorted array of integers a, find an integer x from a such that the value of

abs(a[0] - x) + abs(a[1] - x) + ... + abs(a[a.length - 1] - x)

is the smallest possible (here abs denotes the absolute value). If there are several possible answers, output the smallest one.

Example

For a = [2, 4, 7], the output should be absoluteValuesSumMinimization(a) = 4.

Input/Output

[execution time limit] 4 seconds (js)

[input] array.integer a

A non-empty array of integers, sorted in ascending order.

Guaranteed constraints: 1 ≤ a.length ≤ 200, −10^​6 ≤ a[i] ≤ 10^​6.

[output] integer
"""

"""
    Problem Statement: https://wachino.github.io/codefights/codefights-arcade/codefights-arcade-intro/32_absoluteValuesSumMinimization/README.html
    
    Explanation: https://math.stackexchange.com/questions/113270/the-median-minimizes-the-sum-of-absolute-deviations-the-ell-1-norm
    The median minimizes the sum of absolute deviations.
    The median is the middle value of a sorted array. If the array has an even number of elements, the median is the average of the two middle values.
    
    https://stackoverflow.com/questions/44379453/explaining-the-math-behind-an-algorithm
    
    Solution:
    https://stackoverflow.com/questions/44379453/explaining-the-math-behind-an-algorithm
    
"""

import math

def absoluteValuesSumMinimization(a):
    #return a[len(a)/2]
    # return a[len(a)/2 - 1] if len(a) % 2 == 0 else a[len(a)/2]
    return a[math.ceil(len(a)/2)-1]

if __name__ == '__main__':
    print(absoluteValuesSumMinimization([2, 4, 7]))
    print(absoluteValuesSumMinimization([2, 4, 7, 6]))
    print(absoluteValuesSumMinimization([2, 4, 7, 6, 6]))
    print(absoluteValuesSumMinimization([2, 4, 7, 6, 6, 8]))
    print(absoluteValuesSumMinimization([2, 4, 7, 6, 6, 8, 9]))
    print(absoluteValuesSumMinimization([2, 4, 7, 6, 6, 8, 9, 10]))
    print(absoluteValuesSumMinimization([2, 4, 7, 6, 6, 8, 9, 10, 11]))
    print(absoluteValuesSumMinimization([2, 4, 7, 6, 6, 8, 9, 10, 11, 12]))
    print(absoluteValuesSumMinimization([2, 4, 7, 6, 6, 8, 9, 10, 11, 12, 13]))