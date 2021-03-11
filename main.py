import random
import time

def is_valid(user_input):
    return True if 1 <= user_input <= 100 else False

print('Добро пожаловать в числовую угадайку!')
n = int(input('Введите правую границу для случайного выбора числа: '))
generated = random.randint(1, n)

tries = 7

while True:
    print(f'Осталось {tries} попыток')
    user_input = input('Введите число: ')
    user_input = int(user_input)
    if is_valid(user_input):
        if tries > 1:
            if user_input < generated:
                print('Ваше число меньше загаданного, попробуйте еще разок')
                tries -= 1
            elif user_input > generated:
                print('Ваше число больше загаданного, попробуйте еще разок')
                tries -= 1
            elif user_input == generated:
                print('Вы угадали, поздравляем!')
                again = input('Сыграть еще разок? (да нет)')
                if again == 'да':
                    n = int(input('Введите правую границу для случайного выбора числа: '))
                    generated = random.randint(1, n)
                    tries = 7
                    continue
                elif again == 'нет':
                    break
        else:
            again = input('Упс, попытки закончились. Сыграть еще разок?')
            if again == 'да':
                n = int(input('Введите правую границу для случайного выбора числа: '))
                generated = random.randint(1, n)
                tries = 7
                continue
            elif again == 'нет':
                break
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')
        tries -= 1
        continue

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
time.sleep(3)