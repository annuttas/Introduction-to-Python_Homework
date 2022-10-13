# 4. ** Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# 1. Добавьте игру против бота
# 2. Подумайте как наделить бота "интеллектом"

# Разбор д/з

from random import shuffle, randint

# CANDIES = 2021
CANDIES = 100
CANDIES_LIMIT = 28


def bot_run(candies: int) -> int:
    result = candies % 29 # Бот всегда будет брать остаток от деления на 29. Если он начнёт 1м - вы не выиграете
    if not result:
        result = randint(1, 28)
    return result


def moves(pl_act):
    first, second = players
    return second if pl_act == first else first


players = ["human", 'bot' if int(input('Play with bot 1 - yes, 0 - no? ')) else 'person'] # Собираем спикок участников. У нас может быть только человек и кто-то (person или bot)
shuffle(players) # Перемешиваем игроков

active_player = players[0] # Кто встал на нулевой индекс
print(f'1 player - {players[0]}, 2 player - {players[1]}')

while CANDIES > 0:
    print(f'\nThere are {CANDIES} sweets on the table, you can take [1 .. {CANDIES_LIMIT}]')
    print(f"Player {active_player}'s move")

    if active_player == "bot":
        get_candies = bot_run(CANDIES)
        print(f'The bot took {get_candies} candies')
    else:
        get_candies = int(input(f'How many candies do you want {active_player}: '))

    # проверки
    if get_candies not in range(1, CANDIES_LIMIT + 1):
        print('Wrong move!')
    else:
        CANDIES -= get_candies
        if CANDIES > 0:
            active_player = moves(active_player) # Переключение режима на следующего игрока
        else:
            print(f'The player {active_player} won!') # Иначе, выиграли - конфеток больше нет)