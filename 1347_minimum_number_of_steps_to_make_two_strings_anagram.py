from collections import Counter

def minSteps(s, t):
  first = Counter(s)
  second = Counter(t)

  steps = 0

  for k, v in first.items():
    if k in second and second[k] < v:
      steps += v - second[k]
    elif k not in second:
      steps += v

  return steps


s = 'leetcode'
t = 'practice'

print(minSteps(s, t))