'''cells = ' '.join(input("Enter cells: ")).split(' ')
print(cells)

print("---------")
print("| {} {} {} |".format(cells[0], cells[1], cells[2]))
print("| {} {} {} |".format(cells[3], cells[4], cells[5]))
print("| {} {} {} |".format(cells[6], cells[7], cells[8]))
print("---------")'''

cells = list(input("Enter cells: "))


def table(cells):
    border = '-'
    print(border * 9)
    for i in range(0, 9, 3):
        print('|', *cells[i:i + 3], '|')
    print(border * 9)


def game(cells):
    coordinates = input('Enter the coordinates:').split()
    if coordinates[0] in '0123456789' and coordinates[1] in '0123456789':
        move(int(coordinates[0]), int(coordinates[1]))
    else:
        print("You should enter numbers!")
        return game(cells)


def move(x, y):
    if 1 <= x <= 3 and 1 <= y <= 3:
        if x == 1 and y == 1:
            if cells[6] == '_':
                cells[6] = 'X'
                return table(cells)
            else:
                print("This cell is occupied! Choose another one!")
                return game(cells)
        elif x == 1 and y == 2:
            if cells[3] == '_':
                cells[3] = 'X'
                return table(cells)
            else:
                print("This cell is occupied! Choose another one!")
                return game(cells)
        elif x == 1 and y == 3:
            if cells[0] == '_':
                cells[0] = 'X'
                return table(cells)
            else:
                print("This cell is occupied! Choose another one!")
                return game(cells)
        elif x == 2 and y == 1:
            if cells[7] == '_':
                cells[7] = 'X'
                return table(cells)
            else:
                print("This cell is occupied! Choose another one!")
                return game(cells)
        elif x == 2 and y == 2:
            if cells[4] == '_':
                cells[4] = 'X'
                return table(cells)
            else:
                print("This cell is occupied! Choose another one!")
                return game(cells)
        elif x == 2 and y == 3:
            if cells[1] == '_':
                cells[1] = 'X'
                return table(cells)
            else:
                print("This cell is occupied! Choose another one!")
                return game(cells)
        elif x == 3 and y == 1:
            if cells[8] == '_':
                cells[8] = 'X'
                return table(cells)
            else:
                print("This cell is occupied! Choose another one!")
                return game(cells)
        elif x == 3 and y == 2:
            if cells[5] == '_':
                cells[5] = 'X'
                return table(cells)
            else:
                print("This cell is occupied! Choose another one!")
                return game(cells)
        elif x == 3 and y == 3:
            if cells[2] == '_':
                cells[2] = 'X'
                return table(cells)
            else:
                print("This cell is occupied! Choose another one!")
                return game(cells)
        return table(cells)
    elif (x > 3 or x < 1) or (y > 3 or y < 1):
        print("Coordinates should be from 1 to 3!")
        return game(cells)


table(cells=cells)
game(cells=cells)

'''def impossible(cells):
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
        print('Draw')'''