def greet():
    print('Игру начинает крестик')
    print('Для записи крестика или нолика в определённую клетку,')
    print('необходимо ввести её координаты,')
    print('где первая цифра - номер строки, а вторая - столбца')
    print('от 0 до 2 включительно через пробел.')
    print('Например: 0 2 или 2 1.')
    print()

def show():
    print("  0 1 2")
    for i in range(3):
        print(f"{i} {field[i][0]} {field[i][1]} {field[i][2]}")

def ask():
    while True:
        cords = input("Ходите: ").split()

        if len(cords) != 2:
            print("Введите 2 цифры")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print("Введите цифры")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Координаты вне диапазона")
            continue

        if field[x][y] != " ":
            print("Клетка занята")
            continue

        return x, y

def check_win():
    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[i][j])
            if symbols == ["X", "X", "X"]:
                print("Выиграл X!")
                return True
            if symbols == ["0", "0", "0"]:
                print("Выиграл 0!")
                return True

    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[j][i])
            if symbols == ["X", "X", "X"]:
                print("Выиграл X!")
                return True
            if symbols == ["0", "0", "0"]:
                print("Выиграл 0!")
                return True

    symbols = []
    for i in range(3):
        symbols.append(field[i][i])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!")
            return True

    symbols = []
    for i in range(3):
        symbols.append(field[i][2-i])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!")
            return True

    return False

greet()
field = [[" "] * 3 for i in range(3)]
num = 0
while True:
    num += 1
    show()

    if num % 2 == 1:
        print("Ходит крестик")
    else:
        print("Ходит нолик")

    x, y = ask()

    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if num == 9:
        print("Ничья!")
        break