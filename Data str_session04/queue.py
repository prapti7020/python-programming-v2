#FIFO(first in first out)


# from collections import deque

# queue = deque()
# queue.append(1)
# queue.append(2)
# queue.append(3)

# # print(queue)

# queue.popleft()
# queue.popleft()

# print(queue)






from collections import deque

queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)

print(queue)

queue.popleft()

print(queue)