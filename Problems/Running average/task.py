num = [int(x) for x in input()]
print([(num[x] + num[x + 1]) / 2 for x in range(len(num) - 1)])