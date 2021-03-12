import random

def greetings():
    print('Добро пожаловать в числовую угадайку!')
    n = input('Введите правую границу для случайного выбора числа: ')
    generated = random.randint(1, int(n))
    tries = 7
    return n, generated, tries


def is_valid(user_input, n):
    if user_input.isdigit() and n.isdigit():
        if 1 <= int(user_input) <= int(n):
            return True
    else:
        return False

def play_again():
    while True:
        n = input('Введите правую границу для случайного выбора числа: ')
        if n.isdigit():
            break
        else:
            continue
    generated = random.randint(1, int(n))
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

