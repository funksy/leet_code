def findDifference(nums1, nums2):
    copy, nums1, nums2 = set(nums1), set(nums1), set(nums2)
    for num in copy:
        if num in nums2:
            nums1.remove(num)
            nums2.remove(num)
    return([list(nums1), list(nums2)])


print(findDifference([1,2,3], [2,4,6]))