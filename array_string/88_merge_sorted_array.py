def merge(nums1, m, nums2, n):
    ptr1, ptr2, write_ptr = m - 1, n - 1, m + n - 1

    while ptr2 >= 0:
        if ptr1 >= 0 and nums1[ptr1] > nums2[ptr2]:
            nums1[write_ptr] = nums1[ptr1]
            ptr1 -= 1
        else:
            nums1[write_ptr] = nums2[ptr2]
            ptr2 -=1
        write_ptr -=1


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

merge(nums1, m, nums2, n)
print(nums1)