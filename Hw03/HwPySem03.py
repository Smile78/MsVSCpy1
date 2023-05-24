'''
Задача 16: 
Требуется вычислить, сколько раз встречается некоторое число X в массиве A[N].

Задача 18: 
Требуется найти в массиве A[N] самый близкий по величине элемент к заданному числу X.

Задача 20:
Напишите программу, которая вычисляет стоимость введенного пользователем слова..

'''
import random


def main():
    i = int(0)
    while (i < 1):
        task_16_rep()
        task_18_near_2()
        task_20_lettrs_strt()
        i += 1


def task_20_lettrs_strt():
    print("\n-------------- task20: \' summ prices of letters in word \' ")
    print("for example: we know that word \'ноутбук\' got price: 12 ")
    print("lets try to count its price by machine ")
    word1 = ('ноутбук')
    task_20_lettrs_Base(word1)    
    inp_1 = str(input("Введите своё слово для расчета:"))
    task_20_lettrs_Base(inp_1)    

def task_20_lettrs_Base(wrd: str):
    word = str.lower(wrd)
    wordSpel = list(word)
    # print(wordSpel)
    dim1ltrsL1 = task_20_base_convertStr(1)
    dim1ltrsL2 = task_20_base_convertStr(2)
    dim1ltrsL3 = task_20_base_convertStr(3)
    dim1ltrsL4 = task_20_base_convertStr(4)
    dim1ltrsL5 = task_20_base_convertStr(5)
    dim1ltrsL8 = task_20_base_convertStr(8)
    dim1ltrsL10 = task_20_base_convertStr(10)
    # print(dim1ltrsL1)
    totalScore = int(0)
    # TODO на словаре все вместе?
    for w in wordSpel:
        for l in dim1ltrsL1:
            if w == l:
                totalScore += 1
        for l2 in dim1ltrsL2:
            if w == l2:
                totalScore += 2
        for l3 in dim1ltrsL3:
            if w == l3:
                totalScore += 3
        for l4 in dim1ltrsL4:
            if w == l4:
                totalScore += 4
        for l5 in dim1ltrsL5:
            if w == l5:
                totalScore += 5
        for l8 in dim1ltrsL8:
            if w == l8:
                totalScore += 8
        for l10 in dim1ltrsL10:
            if w == l10:
                totalScore += 10
    print("После подсчета букв с ценой от 1 до 10, стоимость слова \'%s\', составляет:%d\n--------------\n" %
          (wrd, totalScore))


def task_20_base_convertStr(x: int) -> list:
    str1 = "A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т"
    str2 = "D, G, Д, К, Л, М, П, У"
    str3 = "B, C, M, P, Б, Г, Ё, Ь, Я"
    str4 = "F, H, V, W, Y , Й, Ы"
    str5 = "K, Ж, З, Х, Ц, Ч"
    str8 = "J, X, Ш, Э, Ю"
    str10 = "Q, Z, Ф, Щ, Ъ"
    list_str_1 = task_20_convertStr(str1)
    list_str_2 = task_20_convertStr(str2)
    list_str_3 = task_20_convertStr(str3)
    list_str_4 = task_20_convertStr(str4)
    list_str_5 = task_20_convertStr(str5)
    list_str_8 = task_20_convertStr(str8)
    list_str_10 = task_20_convertStr(str10)
    match(x):
        case(1): return [str.lower(i) for i in list_str_1]
        case(2): return [str.lower(i) for i in list_str_2]
        case(3): return [str.lower(i) for i in list_str_3]
        case(4): return [str.lower(i) for i in list_str_4]
        case(5): return [str.lower(i) for i in list_str_5]
        case(8): return [str.lower(i) for i in list_str_8]
        case(10): return [str.lower(i) for i in list_str_10]


def task_20_convertStr(str1: str) -> list:
    strSp = list(str1.split(", "))
    return strSp


def task_18_near_2():
    print("\n-------------- task18: \' search for nearest number \' ")
    inp1 = int(input("Input qnty for array(natural number):"))
    arr1 = [random.randint(-20, 20) for x in range(inp1)]
    print("array: ", arr1)
    inp2 = int(input(
        "Input some number to find out wich number in array is nearest to it(integer):"))
    m1 = max(arr1)
    m2 = min(arr1)
    nrst = int
    nrstDif = max(abs(m1), abs(m2), abs(inp2))
    maxFromMin = m2
    minFromMax = m1

    dif = int

    for i in arr1:
        # если заданое больше нуля
        if inp2 >= 0:
            # если индекс больше нуля
            if i >= 0:
                if inp2 >= i:
                    dif = inp2 - i
                else:
                    dif = i-inp2
                if dif < nrstDif:
                    nrstDif = dif
                    nrst = i
            # если индекс меньше нуля
            else:
                if i > maxFromMin:
                    maxFromMin = i
                    dif = inp2+(abs(i))
                    if dif < nrstDif:
                        nrstDif = dif
                        nrst = maxFromMin
        # если заданое меньше нуля
        else:
            # если индекс меньше нуля
            if i <= 0:
                if inp2 <= i:
                    dif = abs(inp2)-abs(i)
                else:
                    dif = abs(i)-abs(inp2)
                if dif < nrstDif:
                    nrstDif = dif
                    nrst = i
            # если индекс больше нуля
            else:
                if i < minFromMax:
                    minFromMax = i
                    dif = abs(inp2)+i
                    if dif < nrstDif:
                        nrstDif = dif
                        nrst = maxFromMin
    print("ближайшее число из массива:%s к выбранному вами числу:%d это:%d" %
          (arr1, inp2, nrst))
    print("--------------\n")


def task_16_rep():
    # print(arr)
    print("\n-------------- task16: \' retryz inside array \' ")
    inp_1 = int(input("Введите кол-во чисел в массиве:"))
    arr1 = []
    # arr1 = [0]
    for i in range(inp_1):
        arr1.append(random.randint(1, 5))
    print(f"massiv:", arr1)
    inp_2 = int(input("Сообщите о странном числе:"))
    d_note = []
    ind = 0
    for i in arr1:
        if i == inp_2:                  #можно
            d_note.append(ind)
        ind += 1
    # for i in range(len(arr1),0,-1):
    for i in reversed(d_note):
        arr1.pop(i)
    print(f"Вуаля:", arr1)
    print("--------------\n")


if __name__ == "__main__":
    main()
