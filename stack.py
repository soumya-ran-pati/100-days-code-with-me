stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)

item = stack.pop()
print("Popped:", item)

print("Stack after pop:", stack)

# Peek (top element)
print("Top element:", stack[-1])

if len(stack) == 0:
    print("Stack is empty")
