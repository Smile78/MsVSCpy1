'''
Задача 2: 
Найдите сумму цифр трехзначного числа

Задача 4: 
журавлики
Катя сделала в два раза больше журавликов

Задача 6: 
Счастливый билет

Задача 8: 
шоколадки
от шоколадки размером n × m долек 
отломить k долек
'''


import random

import os

def main():
    task_2_sum(123)
    task_2_sum(100)
    task_4_crane(60)
    task_4_crane(24)
    task_4_crane(6)
    task_6_luky_ticket(132123) 
    task_8_chocolates(4, 8, 6)
    
  


def task_8_chocolates(n: int, m: int, k):
    print("\n", "-"*12, "  Task8 \' chocolates \'", sep="")
    print("если без экономии. в 1ый раз можно отломить <= длиной стороне ")
    print("шоколадка %dx%d, надо %d кусочков" % (n, m, k))
    print("можно" if max(n, m) >= k else "нет!")


def task_6_luky_ticket(nmb:int):
    print("\n", "-"*12, "  Task6 \' lucky ticket \'", sep="")
    print("-"*12, "  Task6 !!!антидекоратор!!!---------------- для расчета суммы используется 2ой таск. такчто будет два принта из 2го таска!!!", sep="")
    lnm=nmb//1000
    rnm=nmb%1000 
    lsum=task_2_sum(lnm)
    rsum=task_2_sum(rnm)
    print("-"*12, "  Task6 !!!антидекоратор END!!! -----------дальше принты 6го таска\nРезультат:", sep="")
    if lsum==rsum: print(":вот это удача, офигеть")
    else: print("а мог бы и кирпич на голову упасть")

def task_4_crane(s: int):
    print("\n", "-"*12, "  Task4 \' cranes \'", sep="")
    kQ = s*2/3
    pQ = kQ/4
    sQ = kQ/4
    # print("given sum of cranes:%d\nKatya's quantity:%d\nPetya's quantity:%d\nSerega's quantity:%d \n" % (s,kQ,pQ,sQ))
    print("%d -> %d, %d, %d \n" % (s, pQ, kQ, sQ))


def task_2_sum(x: int):
    list1s = list(str(x))
    # list1d= [int(i) for i in list1s]
    sum = int(0)
    lx = list([int(i) for i in list1s])
    for i in lx:
        sum += i
    print("\n", "-"*12, "  Task2 \' the sum of digits in number \'", sep="")
    print("given the number:%d \nthe sum of its digits is:%d\n" % (x, sum))






def dif_symb(str1: str, str2: str):
    cnt = int(0)
    for i in str1:
        if i not in str2:
            print(
                "во второй нет вот этого символа из первой:%s, указатель! в первой:%s" % (i, cnt))
    cnt = int(-1)
    for i in str2:
        cnt += 1
        if i not in str1:
            print(
                "в первой нет вот этого символа из второй:%s, указатель! во второй:%s" % (i, cnt))
            print(str2)
            print(" "*(cnt-1), "^")  # потомучто проьелов то меньше )


def rus_symb(str1: str):
    # print("----wtf---")
    alfRus = str("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
    # print("alfRus long:",len(alfRus))
    str2 = str1.lower()
    for i in str2:
        if i in alfRus:
            print("вот и рус символ:", i)



if __name__ == "__main__":
    main()
