from collections import deque

class RecentCounter:
    def __init__(self):
        self.requests = deque()

    def ping(self, t):
        self.requests.append(t)
        while self.requests[0] < t - 3000:
            self.requests.popleft()
        return len(self.requests)


test = RecentCounter()
print(test.ping(1))
print(test.ping(2))
print(test.ping(3))
print(test.ping(4))
print(test.ping(3000))