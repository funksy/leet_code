class MyQueue:
  def __init__(self):
    self.stack1 = []
    self.stack2 = []

  def push(self, x):
    self.stack1.append(x)

  def pop(self):
    for i in range(len(self.stack1) - 1):
      self.stack2.append(self.stack1.pop())
    
    res = self.stack1.pop()

    for i in range(len(self.stack2)):
      self.stack1.append(self.stack2.pop())
    
    return res

  def peek(self):
    return self.stack1[0]

  def empty(self):
    return len(self.stack1) == 0


test_stack = MyQueue()
print(test_stack.empty())
test_stack.push(1)
print(test_stack.empty())
test_stack.push(2)
print(test_stack.pop())
test_stack.push(3)
print(test_stack.pop())
print(test_stack.peek())
print(test_stack.pop())
print(test_stack.empty())