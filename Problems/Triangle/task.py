n = int(input())
L = ['#']
for i in range(1, 2 * n - 1, 2):
    L.append('#' * (i + 2))

for i in range(len(L)):
    print(L[i].center(2 * n - 1))

'''n = int(input()) * 2
for i in range(1, n, 2):
    print(('#' * i).center(n - 1))'''