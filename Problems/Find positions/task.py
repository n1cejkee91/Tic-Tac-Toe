# put your python code here
numbers = input().split()
x = input()

if x in numbers:
    for i in range(len(numbers)):
        if x == numbers[i]:
            print(i, end=' ')
else:
    print('not found')