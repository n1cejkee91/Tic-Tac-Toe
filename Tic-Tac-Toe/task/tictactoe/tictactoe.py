'''cells = ' '.join(input("Enter cells: ")).split(' ')
print(cells)

print("---------")
print("| {} {} {} |".format(cells[0], cells[1], cells[2]))
print("| {} {} {} |".format(cells[3], cells[4], cells[5]))
print("| {} {} {} |".format(cells[6], cells[7], cells[8]))
print("---------")'''



cells = list(input("Enter cells: "))

border = '-'
print(border * 9)
for i in range(0, 9, 3):
    print('|', *cells[i:i + 3], '|')
print(border * 9)