# Задача 10:
# На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
#
## Задача 12:
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
#
# Задача 14:
# Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.


import random


def main():
    tsk10_monetki()
    tsk12_mult()
    tsk14_pwr()


def tsk14_pwr():
    inp1 = (int(input("\n------------Task14 \' show all included pows of 2 \' \nInput number:")))
    x = 1
    while (2 ** x < inp1):
       print(f"2 ^ {x:3} = {(2 ** x):16_d} ")
       x+=1
    print(f"input: {(inp1):19_d} ")


def tsk12_mult():
    xRng = 10010

    ch1: int = random.randint(1, xRng)
    ch2: int = random.randint(1, xRng)
    hpl1Sum = ch1 + ch2
    hpl2Mult = ch1 * ch2

    rsltList: dict = ({0: 0});

    print("\n------------Task12 \' random numbers to multiply and summary \'\nchs1=%d chs2=%d sum=%d mult=%d" % (
        ch1, ch2, hpl1Sum, hpl2Mult))

    for mlt1 in range(1, xRng):
        for mlt2 in range(1, xRng):
            if (mlt1 * mlt2) == hpl2Mult and (mlt1 > mlt2): break;
            if (mlt1 * mlt2) == hpl2Mult and mlt1 + mlt2 == hpl1Sum: rsltList.update({mlt1: mlt2})
    rsltList.pop(0)
    print('common numbers=', rsltList)


def tsk10_monetki():
    n: int = int(input("\n------------Task10 \' monetki \' \nInput coins qntty:"))
    massCoins = [random.randint(0, 1) for _ in range(n)]
    qntCoins: int = 0
    for i in massCoins:
        if i: qntCoins += 1 # if i true????????????????????
    rslt: int = 0
    rslt = (n - qntCoins) if (qntCoins > (n / 2)) else qntCoins
    print("всего монеток:%d \nорлом выпало:%d \nмин кол-во монеток на переворот:%d " % (n, qntCoins, rslt))


if __name__ == '__main__':
    main()
