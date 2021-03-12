import random

def greetings():
    print('Добро пожаловать в числовую угадайку!')
    n = int(input('Введите правую границу для случайного выбора числа: '))
    generated = random.randint(1, n)
    tries = 7
    return n, generated, tries


def is_valid(user_input, n):
    return True if 1 <= user_input <= n else False

def play_again():
    while True:
        n = input('Введите правую границу для случайного выбора числа: ')
        if n.isdigit():
            break
        else:
            continue
    n = int(n)
    generated = random.randint(1, n)
    tries = 7
    return n, generated, tries

def check_again():
    while True:
        again = input('Сыграть еще разок? (да нет)')
        if again == 'да' or again == 'нет':
            break
        else:
            continue
    return again

