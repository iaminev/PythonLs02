'''Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток,
которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть'''
import math


def coins():
    print("Переворачиваем монеты")
    total_coins = int(input('Введите количество монет: '))
    heads = int(input('Введите количество монет, которые лежат орлом: '))
    tails = total_coins - heads

    if (heads > total_coins):
        print(f'Количество монет введено ошибочно (орлов больше, чем всего монет)')
    elif (heads == total_coins) | (heads==0):
        print(f'Ничего переворачивать не надо')
    else:
        print(f'Необходимо перевернуть монет: {min(heads, tails)}')
    print("\n")

'''Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.'''

def guess_numbers():
    print("Угадываем числа")
    sum_x_y = int(input('Введите сумму чисел: '))
    product_x_y = int(input('Введите произведение чисел: '))

    solution_found = False


    for x in range(1,sum_x_y):
        for y in range(1, sum_x_y):
            if (x + y == sum_x_y) & (x * y == product_x_y) & (not solution_found):
                print(f'Результат: x={x}, y={y}')
                solution_found = True
    if (not solution_found):
        print(f'Нет решения!')
    print("\n")


'''Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.'''

def powers_of_two():
    print("Ищем целые степени двойки")
    N = int(input('Введите число, до которого необходимо вывести целые степени двойки: '))

    cur_power = 0
    cur_result = math.pow(2,cur_power)
    while cur_result <= N:
        print(f'{cur_result:.0f}, ', end='')
        cur_power+=1
        cur_result = math.pow(2, cur_power)
    print("\n")

if __name__ == '__main__':
    coins()
    guess_numbers()
    powers_of_two()

