from collections import Counter

def singleNumber(nums):
    counts = Counter(nums)
    for k, v in counts.items():
        if v == 1:
            return k

    # ! example of using the XOR operator
    # res = 0
    # for num in nums:
    #     res ^= num

    # return res




nums = [2, 2, 1]
print(singleNumber(nums))