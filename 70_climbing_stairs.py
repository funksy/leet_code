def climbStairs(n):
  res = 1
  prev = res

  for i in range(1, n):
    res, prev = res + prev, res
  
  return res

n = 5
print(climbStairs(n))