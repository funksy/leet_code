def kidsWithCandies(candies, extraCandies):
    max_candies = max(candies)
    results = []
    for i in range(len(candies)):
        results.append(candies[i] + extraCandies >= max_candies)
    return results


print(kidsWithCandies([2,3,5,1,3], 3))