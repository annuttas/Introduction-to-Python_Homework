# 3. * Создайте программу для игры в "Крестики-нолики". 
# Поле 3x3. Игрок - игрок, без бота.

# Разбор д/з

board = list(map(str, range(1, 10)))


def draw_board():  # Отрисовка поля или доски
    print('-' * 20)
    for i in range(3):
        for k in range(3):
            print(f"{board[k + i * 3]:^5}", end=" ")
        print(f"\n{'-' * 20}")
    print()


def place_sign(token): # Размещение крестика и нолика
    global board
    while True:
        answer = input(f"Enter a number from 1 to 9.\nSelect a position {token}? ")
        if answer.isdigit() and int(answer) in range(1, 10):
            answer = int(answer)
            pos = board[answer - 1]
            if pos not in (chr(10060), chr(11093)):
                board[answer - 1] = chr(10060) if token == "X" else chr(11093) # Тернарный оператор. Если истина, мы делаем то, что слева, если ложно, мы делаем то, что после else (справа)
                break
            else:
                print(f"This cell is already occupied{chr(9995)}{chr(129292)}")
        else:
            print(f"Incorrect input{chr(9940)}. Are you sure you entered a correct number?")


def check_win(): # Выйгрышные позиции
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)) # Индексы всевозможных выигрышных позиций
    n = [board[x[0]] for x in win_coord if board[x[0]] == board[x[1]] == board[x[2]]] # list comprehension. Проверка условия, если совпадение значений в ячейках по данным индексам, то выигрыш
    return n[0] if n else n # Тернарный оператор


def main():  # Основое меню
    counter = 0 # Чередуемся просто переключая х/0, у нас нет бота, работа идёт в автоматическом режиме
    draw_board() # Отрисовка доски
    while True:
        place_sign("O") if counter % 2 else place_sign("X") # Чередование хода. Осуществляется с помощью тернарного оператора. Если ход нечётный - ходит 0, если чётный - Х
        draw_board()

        if counter > 3:  # Количество ходов перешло за 3
            if check_win():
                print(f"{check_win()} - WIN{chr(127942)}{chr(127881)}!")
                break
        if counter == 8: # Выводим ничья
            print(f"Drawn game {chr(129318)}{chr(129309)}!")
            break
        counter += 1
main()