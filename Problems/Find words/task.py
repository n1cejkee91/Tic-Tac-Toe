sentense = input().split()
word = []
for i in sentense:
    if i.endswith('s'):
        word.append(i)
new_word = '_'.join(word)
print(new_word)