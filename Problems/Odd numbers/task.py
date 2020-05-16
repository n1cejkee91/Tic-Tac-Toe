digits = list(input())
new_digits = [int(i) for i in digits if int(i) % 2 == 1]
print(new_digits)