# Queqes
Q.1
from collections import deque

def reverse_first_three(q):
    stack = []
    for _ in range(3):
        stack.append(q.popleft())
    while stack:
        q.appendleft(stack.pop())
    return q

q = deque([1, 2, 3, 4, 5])
print(reverse_first_three(q))


#Q2
from collections import deque

q = deque()

while True:
    user_input = input("Enter a number (empty to stop): ")

    if user_input == "":
        break

    num = int(user_input)
    q.append(num)

    # Keep only last 5
    if len(q) > 5:
        q.popleft()

print("Final queue:", list(q))

#Q3
from collections import deque

def round_robin(tasks):
    q = deque(tasks)
    finished = []

    while q:
        name, time_left = q.popleft()

        # Give 2 units of work
        time_left -= 2

        if time_left > 0:
            q.append((name, time_left))   # put back with remaining time
        else:
            finished.append(name)         # task completed

    return finished


# Example
tasks = [("A", 3), ("B", 6), ("C", 1)]
print(round_robin(tasks))   # ['A', 'C', 'B']


# stacks
Q1

def find_min(stack):
    if not stack:
        print("Stack is empty")
        return

    print(min(stack))


# Example
stack = [5, 2, 9, 1, 7]
find_min(stack)   # Output: 1

Q2
def undo_actions(actions, n):
    undone = []

    for _ in range(n):
        if actions:                 # check stack not empty
            undone.append(actions.pop())
        else:
            break

    return undone, actions


# Example
actions = ["open", "edit", "save", "close"]
undone, remaining = undo_actions(actions, 2)

print("Undone:", undone)           # ['close', 'save']
print("Left in stack:", remaining) # ['open', 'edit']

Q3
def simplify_path(path):
    parts = path.split("/")
    stack = []

    for part in parts:
        if part == "" or part == ".":
            continue
        elif part == "..":
            if stack:
                stack.pop()
        else:
            stack.append(part)

    return "/" + "/".join(stack)


# Example
print(simplify_path("/home//user/.././docs"))   # /home/docs
