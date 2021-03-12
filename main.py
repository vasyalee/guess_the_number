import random
import time
from functions import *


n, generated, tries = greetings()

while True:
    print(f'Осталось {tries} попыток')
    user_input = input('Введите число: ')
    user_input = int(user_input)
    if is_valid(user_input, n):
        if tries > 1:
            if user_input < generated:
                print('Ваше число меньше загаданного, попробуйте еще разок')
                tries -= 1
            elif user_input > generated:
                print('Ваше число больше загаданного, попробуйте еще разок')
                tries -= 1
            elif user_input == generated:
                print('Вы угадали, поздравляем!')
                again = check_again()
                if again == 'да':
                    n, generated, tries = play_again()
                    continue
                elif again == 'нет':
                    break
        else:
            print('Упс, попытки закончились.')
            again = check_again()
            if again == 'да':
                n, generated, tries = play_again()
                continue
            elif again == 'нет':
                break
    else:
        print(f'А может быть все-таки введем целое число от 1 до {n}?')
        tries -= 1
        continue

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
time.sleep(3)