import random

class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.nums_map = {}

    def insert(self, val):
        if val in self.nums_map:
            return False
        
        self.nums.append(val)
        self.nums_map[val] = len(self.nums) - 1
        return True

    def remove(self, val):
        if val not in self.nums_map:
            return False
            
        last_ele = self.nums[-1]
        remove_index = self.nums_map[val]
        self.nums_map[last_ele] = remove_index
        self.nums[remove_index] = last_ele
        self.nums.pop()
        self.nums_map.pop(val)
        return True


    def getRandom(self):
        return random.choice(self.nums)


test = RandomizedSet()
print(test.remove(0))
print(test.remove(0))
print(test.insert(0))
print(test.getRandom())
print(test.remove(0))
print(test.insert(0))