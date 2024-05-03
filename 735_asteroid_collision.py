def asteroidCollision(asteroids):
    stack = []
    for asteroid in asteroids:
        while stack and stack[-1] > 0 and asteroid < 0:
            if stack[-1] + asteroid < 0:
                stack.pop()
            elif stack[-1] + asteroid > 0:
                break
            else:
                stack.pop()
                break
        else:
            stack.append(asteroid)
    return stack


test1 = [10,2,-5]
test2 = [8,-8]

print(asteroidCollision(test1))