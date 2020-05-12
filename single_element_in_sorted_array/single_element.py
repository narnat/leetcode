#!/usr/bin/env python3


def singleNonDuplicate(nums):
    '''
    Simple binary search, checking all boundaries and
    using index to determine which part of array to go
    '''
    start, end = 0, len(nums) - 1

    while start <= end:
        mid = (start + end) // 2
        if ((mid == 0 or nums[mid - 1] != nums[mid]) and
            (mid == len(nums) - 1 or
             nums[mid + 1] != nums[mid])):
            return nums[mid]
        if ((mid % 2 == 1 and nums[mid - 1] == nums[mid]) or
            (mid % 2 == 0 and (mid < len(nums) - 1 and
            nums[mid + 1] == nums[mid]))):
            start = mid + 1
        else:
            end = mid - 1


def singleNonDuplicate_1(nums):
    '''
    Binary search, getting pairs, if current pair is equal to each other
    advance left part up to mid pairs does not have single element,
    if they are not equal then left part up to mid pair contains single
    element, thus @end = @mid
    '''
    start, end = 0, len(nums) // 2

    while start < end:
        mid = start + (end - start) // 2
        if nums[2 * mid] == nums[2 * mid + 1]:
            start = mid + 1
        else:
            end = mid

    return nums[2 * start]


def singleNonDuplicate_2(nums):
    '''
    Binary search
    '''
    start, end = 0, len(nums) - 1

    while start < end:
        mid = start + (end - start) // 2
        # Make mid even
        if mid % 2:
            mid -= 1
        if nums[mid] == nums[mid + 1]:
            # we know that mid and mid + 1 are pairs
            # thus adding two
            start = mid + 2
        else:
            end = mid

    return nums[start]


def singleNonDuplicate_3(nums):
    '''
    Binary search
    '''
    start, end = 0, len(nums) - 1

    while start < end:
        mid = start + (end - start) // 2
        # using xor trick
        # if n is odd, n ^ 1 will be n - 1
        # if n is even, n ^ 1 will be n + 1
        if nums[mid] == nums[mid ^ 1]:
            start = mid + 1
        else:
            end = mid

    return nums[start]
