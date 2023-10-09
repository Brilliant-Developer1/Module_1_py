# Set is unique items
numbers = [12, 55, 44, 55, 11, 10, 58, 96, 11, 47]
numbers_set = set(numbers)
print(numbers)
print(numbers_set)
numbers_set.add(100)
print(numbers_set)
numbers_set.remove(44)
print(numbers_set)

# Common in A and B
A = {1, 3, 5}
B = {1, 2, 3, 4, 5}
print(A & B)
print(A | B)
