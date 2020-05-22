word = input().split('_')
W = []
for i in word:
    W.append(i.capitalize())
print(''.join(W))