from collections import Counter

def majorityElement(nums):
    for key, val in Counter(nums).items():
            if val > len(nums) / 2:
                return key


nums = [3,2,3]

print(majorityElement(nums))