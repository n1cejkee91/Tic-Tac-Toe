'''cells = ' '.join(input("Enter cells: ")).split(' ')
print(cells)

print("---------")
print("| {} {} {} |".format(cells[0], cells[1], cells[2]))
print("| {} {} {} |".format(cells[3], cells[4], cells[5]))
print("| {} {} {} |".format(cells[6], cells[7], cells[8]))
print("---------")'''

'''cells = list(input("Enter cells: "))

border = '-'
print(border * 9)
for i in range(0, 9, 3):
    print('|', *cells[i:i + 3], '|')
print(border * 9)'''

'''M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(len(M)):
    for j in range(len(M)):
        print(M[i][j], end=' ')
    print()'''

cells = list(input("Enter cells: "))

border = '-'
print(border * 9)
for i in range(0, 9, 3):
    print('|', *cells[i:i + 3], '|')
print(border * 9)


def game(cells):
    if '_' in cells:
        if impossible(cells) == 'Impossible':
            print('Impossible')
        else:
            wins1(cells)
    elif '_' not in cells:
        if impossible(cells) == 'Impossible':
            print('Impossible')
        else:
            wins2(cells)


def impossible(cells):
    if (cells.count('O') != cells.count('X')) and (
            cells.count('O') != cells.count('X') - 1 and cells.count('X') != cells.count('O') - 1):
        return 'Impossible'
    elif cells[0] == cells[1] == cells[2] and cells[3] == cells[4] == cells[5] or cells[0] == cells[1] == cells[2] and \
            cells[6] == cells[7] == cells[8] or cells[3] == cells[4] == cells[5] and cells[6] == cells[7] == cells[8] or \
            cells[0] == cells[3] == cells[6] and cells[1] == cells[4] == cells[7] or cells[0] == cells[3] == cells[
        6] and cells[2] == cells[5] == cells[8] or cells[1] == cells[4] == cells[7] and cells[2] == cells[5] == cells[
        8]:
        return 'Impossible'


def wins1(cells):
    if cells[0] == cells[1] == cells[2]:
        print(cells[0], 'wins')
    elif cells[3] == cells[4] == cells[5]:
        print(cells[3], 'wins')
    elif cells[6] == cells[7] == cells[8]:
        print(cells[6], 'wins')
    elif cells[0] == cells[3] == cells[6]:
        print(cells[0], 'wins')
    elif cells[1] == cells[4] == cells[7]:
        print(cells[1], 'wins')
    elif cells[2] == cells[5] == cells[8]:
        print(cells[2], 'wins')
    elif cells[0] == cells[4] == cells[8]:
        print(cells[0], 'wins')
    elif cells[2] == cells[4] == cells[6]:
        print(cells[2], 'wins')
    else:
        print('Game not finished')


def wins2(cells):
    if cells[0] == cells[1] == cells[2]:
        print(cells[0], 'wins')
    elif cells[3] == cells[4] == cells[5]:
        print(cells[3], 'wins')
    elif cells[6] == cells[7] == cells[8]:
        print(cells[6], 'wins')
    elif cells[0] == cells[3] == cells[6]:
        print(cells[0], 'wins')
    elif cells[1] == cells[4] == cells[7]:
        print(cells[1], 'wins')
    elif cells[2] == cells[5] == cells[8]:
        print(cells[2], 'wins')
    elif cells[0] == cells[4] == cells[8]:
        print(cells[0], 'wins')
    elif cells[2] == cells[4] == cells[6]:
        print(cells[2], 'wins')
    else:
        print('Draw')


game(cells=cells)

