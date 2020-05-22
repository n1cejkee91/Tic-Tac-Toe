cells = ['_' for i in range(9)]

def table(cells):
    border = '-'
    print(border * 9)
    for i in range(0, 9, 3):
        print('|', *cells[i:i + 3], '|')
    print(border * 9)

def game(cells):
    if "_" in cells:
        coordinates = input('Enter the coordinates:').split()
        if coordinates[0] in '0123456789' and coordinates[1] in '0123456789':
            if 'X' not in cells and 'O' not in cells:
                moveX(int(coordinates[0]), int(coordinates[1]))
            elif cells.count('X') > cells.count('O'):
                moveO(int(coordinates[0]), int(coordinates[1]))
            else:
                moveX(int(coordinates[0]), int(coordinates[1]))
        else:
            print("You should enter numbers!")
            return game(cells)

def exit():
    pass

def wins1(cells):
    if cells[0] == cells[1] == cells[2] != '_':
        print(cells[0], 'wins')
        return exit()
    elif cells[3] == cells[4] == cells[5] != '_':
        print(cells[3], 'wins')
        return exit()
    elif cells[6] == cells[7] == cells[8] != '_':
        print(cells[6], 'wins')
        return exit()
    elif cells[0] == cells[3] == cells[6] != '_':
        print(cells[0], 'wins')
        return exit()
    elif cells[1] == cells[4] == cells[7] != '_':
        print(cells[1], 'wins')
        return exit()
    elif cells[2] == cells[5] == cells[8] != '_':
        print(cells[2], 'wins')
        return exit()
    elif cells[0] == cells[4] == cells[8] != '_':
        print(cells[0], 'wins')
        return exit()
    elif cells[2] == cells[4] == cells[6] != '_':
        print(cells[2], 'wins')
        return exit()
    else:
        return game(cells)

def wins2(cells):
    if cells[0] == cells[1] == cells[2]:
        print(cells[0], 'wins')
        return exit()
    elif cells[3] == cells[4] == cells[5]:
        print(cells[3], 'wins')
        return exit()
    elif cells[6] == cells[7] == cells[8]:
        print(cells[6], 'wins')
        return exit()
    elif cells[0] == cells[3] == cells[6]:
        print(cells[0], 'wins')
        return exit()
    elif cells[1] == cells[4] == cells[7]:
        print(cells[1], 'wins')
        return exit()
    elif cells[2] == cells[5] == cells[8]:
        print(cells[2], 'wins')
        return exit()
    elif cells[0] == cells[4] == cells[8]:
        print(cells[0], 'wins')
        return exit()
    elif cells[2] == cells[4] == cells[6]:
        print(cells[2], 'wins')
        return exit()
    else:
        print('Draw')
        return exit()

def moveX(x, y):
    if 1 <= x <= 3 and 1 <= y <= 3:
        if x == 1 and y == 1:
            if cells[6] == '_':
                cells[6] = 'X'
                table(cells)
                if '_' in cells:
                    return wins1(cells)
                else:
                    return wins2(cells)
            else:
                print("This cell is occupied! Choose another one!")
                return game(cells)
        elif x == 1 and y == 2:
            if cells[3] == '_':
                cells[3] = 'X'
                table(cells)
                if '_' in cells:
                    return wins1(cells)
                else:
                    return wins2(cells)
            else:
                print("This cell is occupied! Choose another one!")
                return game(cells)
        elif x == 1 and y == 3:
            if cells[0] == '_':
                cells[0] = 'X'
                table(cells)
                if '_' in cells:
                    return wins1(cells)
                else:
                    return wins2(cells)
            else:
                print("This cell is occupied! Choose another one!")
                return game(cells)
        elif x == 2 and y == 1:
            if cells[7] == '_':
                cells[7] = 'X'
                table(cells)
                if '_' in cells:
                    return wins1(cells)
                else:
                    return wins2(cells)
            else:
                print("This cell is occupied! Choose another one!")
                return game(cells)
        elif x == 2 and y == 2:
            if cells[4] == '_':
                cells[4] = 'X'
                table(cells)
                if '_' in cells:
                    return wins1(cells)
                else:
                    return wins2(cells)
            else:
                print("This cell is occupied! Choose another one!")
                return game(cells)
        elif x == 2 and y == 3:
            if cells[1] == '_':
                cells[1] = 'X'
                table(cells)
                if '_' in cells:
                    return wins1(cells)
                else:
                    return wins2(cells)
            else:
                print("This cell is occupied! Choose another one!")
                return game(cells)
        elif x == 3 and y == 1:
            if cells[8] == '_':
                cells[8] = 'X'
                table(cells)
                if '_' in cells:
                    return wins1(cells)
                else:
                    return wins2(cells)
            else:
                print("This cell is occupied! Choose another one!")
                return game(cells)
        elif x == 3 and y == 2:
            if cells[5] == '_':
                cells[5] = 'X'
                table(cells)
                if '_' in cells:
                    return wins1(cells)
                else:
                    return wins2(cells)
            else:
                print("This cell is occupied! Choose another one!")
                return game(cells)
        elif x == 3 and y == 3:
            if cells[2] == '_':
                cells[2] = 'X'
                table(cells)
                if '_' in cells:
                    return wins1(cells)
                else:
                    return wins2(cells)
            else:
                print("This cell is occupied! Choose another one!")
                return game(cells)
    elif (x > 3 or x < 1) or (y > 3 or y < 1):
        print("Coordinates should be from 1 to 3!")
        return game(cells)

def moveO(x, y):
    if 1 <= x <= 3 and 1 <= y <= 3:
        if x == 1 and y == 1:
            if cells[6] == '_':
                cells[6] = 'O'
                table(cells)
                if '_' in cells:
                    return wins1(cells)
                else:
                    return wins2(cells)
            else:
                print("This cell is occupied! Choose another one!")
                return game(cells)
        elif x == 1 and y == 2:
            if cells[3] == '_':
                cells[3] = 'O'
                table(cells)
                if '_' in cells:
                    return wins1(cells)
                else:
                    return wins2(cells)
            else:
                print("This cell is occupied! Choose another one!")
                return game(cells)
        elif x == 1 and y == 3:
            if cells[0] == '_':
                cells[0] = 'O'
                table(cells)
                if '_' in cells:
                    return wins1(cells)
                else:
                    return wins2(cells)
            else:
                print("This cell is occupied! Choose another one!")
                return game(cells)
        elif x == 2 and y == 1:
            if cells[7] == '_':
                cells[7] = 'O'
                table(cells)
                if '_' in cells:
                    return wins1(cells)
                else:
                    return wins2(cells)
            else:
                print("This cell is occupied! Choose another one!")
                return game(cells)
        elif x == 2 and y == 2:
            if cells[4] == '_':
                cells[4] = 'O'
                table(cells)
                if '_' in cells:
                    return wins1(cells)
                else:
                    return wins2(cells)
            else:
                print("This cell is occupied! Choose another one!")
                return game(cells)
        elif x == 2 and y == 3:
            if cells[1] == '_':
                cells[1] = 'O'
                table(cells)
                if '_' in cells:
                    return wins1(cells)
                else:
                    return wins2(cells)
            else:
                print("This cell is occupied! Choose another one!")
                return game(cells)
        elif x == 3 and y == 1:
            if cells[8] == '_':
                cells[8] = 'O'
                table(cells)
                if '_' in cells:
                    return wins1(cells)
                else:
                    return wins2(cells)
            else:
                print("This cell is occupied! Choose another one!")
                return game(cells)
        elif x == 3 and y == 2:
            if cells[5] == '_':
                cells[5] = 'O'
                table(cells)
                if '_' in cells:
                    return wins1(cells)
                else:
                    return wins2(cells)
            else:
                print("This cell is occupied! Choose another one!")
                return game(cells)
        elif x == 3 and y == 3:
            if cells[2] == '_':
                cells[2] = 'O'
                table(cells)
                if '_' in cells:
                    return wins1(cells)
                else:
                    return wins2(cells)
            else:
                print("This cell is occupied! Choose another one!")
                return game(cells)
    elif (x > 3 or x < 1) or (y > 3 or y < 1):
        print("Coordinates should be from 1 to 3!")
        return game(cells)


table(cells)
game(cells)