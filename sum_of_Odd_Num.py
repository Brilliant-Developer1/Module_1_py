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
