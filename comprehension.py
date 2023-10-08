

numbers = [10,15,20,27,30,5,45,40,37,36]
odds=[]
for num in numbers :
    if num % 2 == 1 and num % 5 == 0:
        odds.append(num)

# print(odds)

odd_nums = [num for num in numbers if num % 2 == 1 and num % 5 == 0]
print(odd_nums)

players = ['sakib', 'moshfiq', 'kholil']
ages = [35,26,40]

age_comb = []
for player in players:
    # print( 'Player: ', player)
    for age in ages :
        # print(player,age)
        age_comb.append([player,age])
# print(age_comb)

age_comb2 = [[player, age] for player in players for age in ages]
print(age_comb2)