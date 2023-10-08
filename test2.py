
# test = int(input())

# for _ in range(test):

#     N = input()


#     reversed_str = str(N)[::-1]


#     print(*reversed_str)

test = int(input())

for _ in range(test):

    input_str = input().split()
    x, y = map(int, input_str)

    sumOfOdd = 0

    if x > y:
        for num in range(y, x+1):

            if num != y and num != x:
                if num % 2 != 0:

                    sumOfOdd += num
    else:
        for num in range(x, y+1):

            if num != y and num != x:
                if num % 2 != 0:

                    sumOfOdd += num

    print(sumOfOdd)


# 4 5 6 7 8 9 10
# 4 5 6 7 8 9
# for this input =
# 3
# 5 6
# 10 4
# 4 9

# my expected output is =
# 0
# 21
# 12
# but I'm getting this output=
# 5
# 0
# 21

# why?
