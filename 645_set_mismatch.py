def findErrorNums(nums):
  n = len(nums)
  expected_sum = n * (n + 1) // 2
  actual_sum = sum(nums)
  set_sum = sum(set(nums))

  return [actual_sum - set_sum, expected_sum - set_sum]

nums = [1,2,2,4]
print(findErrorNums(nums))