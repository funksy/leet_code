def heightChecker(heights):
  expected = sorted(heights)
  res = 0

  if heights == expected:
    return res

  
  for i in range(len(heights)):
    if heights[i] != expected[i]:
      res += 1

  return res

heights = [1,2,3,4,5]
print(heightChecker(heights))