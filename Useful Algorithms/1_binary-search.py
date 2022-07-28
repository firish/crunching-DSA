def binary_search(arr, key):
    left = 0
    right = len(arr) - 1
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == key:
            return middle
        elif arr[middle] > key:
            right = middle - 1
        else:
            left = middle + 1
    return -1


def binary_search_recursive(arr, key, left, right):
    if left > right:
        return -1
    else:
        middle = (left + right) // 2
        if arr[middle] == key:
            return middle
        elif arr[middle] > key:
            return binary_search_recursive(Arr, key, left=left, right=middle-1)
        else:
            return binary_search_recursive(Arr, key, left=middle+1, right=right)


Arr = [2, 2, 5, 7, 8, 9, 12, 22]
print(binary_search(Arr, 12))
print(binary_search_recursive(Arr, 12, left=0, right=len(Arr)))


# some useful templates by leet code
# First, Basic template
def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # End Condition: left > right
    return -1

# second template
