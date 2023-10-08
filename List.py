

numbers = [10,15,20,25,30,5,45,40,35,36]
numbers.sort()

print(numbers[3], numbers[-3])

# list( start : end )
print('star to end',numbers[2:6])
# star index to end
print('star index to end', numbers[4:])
# to end index
print('to end index',numbers[:5])

# list( start : end : step )
print(numbers[2:6:2])

#  revers print
print(numbers[7:2:-1])
#  revers print full array
print('revers print full array',numbers[::-1])

# print all
print('print all' ,numbers[:])