from collections import deque

fruits = ['orange', 'apple', 'apple', 'pear', 'banana', 'mango', 'kiwi']

print(fruits.count('apple'))

print(fruits.pop())

print(fruits)

queue = deque(['Eric', 'Michael', 'John'])
queue.append('Jerry')

print(queue)

print(queue.popleft())
print(queue.pop())
print(queue)
