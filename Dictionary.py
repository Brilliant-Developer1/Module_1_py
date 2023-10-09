
numbers = [12, 55, 44, 55, 11, 10, 58, 96, 11, 47]
person = ['Amin', 'Gazipur', 23, 'Student']

person1 = {
    'name': 'Amina',
    'Address': 'Borishal',
    'Age': '20',
    'job': 'Student'

}

print(person1)
print(person1['Address'])
print(person1.keys())
print(person1.values())

person1['class'] = 10
person1['name'] = 'jhamela'
# Delete Age
del person1['Age']
print(person1)

for key, val in person1.items():
    print(key, val)

