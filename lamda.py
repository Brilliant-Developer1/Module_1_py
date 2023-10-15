
# def double(x):
#     return x*2

# alternate of doublr function
# double = lambda x : x * 2
def double(x): return x * 2


res = double(40)
# print(res)

# do some operation into the full array with map
numbers = [12, 55, 44, 55, 11, 10, 58, 96, 11, 47]

# double_nums = map(double, numbers)
double_nums = map(lambda x: x * 2, numbers)
print(list(double_nums))

# print names age bellow 20
actors = [
    {'name': 'sakib', 'age': 35},
    {'name': 'kamal', 'age': 15},
    {'name': 'taalla', 'age': 60},
    {'name': 'james', 'age': 10},
]

juniors = filter(lambda x: x['age'] < 20, actors)

print(list(juniors))
