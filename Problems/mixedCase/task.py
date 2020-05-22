word = input().split()
L = [word[0]]
for i in word[1:]:
    L.append(i.title())
print(''.join(L))

#print("".join(i).title(), end="")