# find maximum sum of a subarray in a single pass, O(n)
# figure out when to leave a subarray because of negative numbers

A = [-1, 8, -5, 7, 2, 4, -1, 4, -3, 5, -12, 11, -4, 2]


def maxSubArray(nums):
    maxi = float('-inf')
    curr = 0
    for i in range(len(nums)):
        curr += nums[i]
        maxi = max(maxi, curr)
        if curr <= 0: curr = 0  # start a new subarray
    return maxi

print(maxSubArray(A))

