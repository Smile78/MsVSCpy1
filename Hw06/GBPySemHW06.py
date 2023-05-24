

""" Задача 30:     an = a1 + (n-1) * d
"""

""" Задача 32:     индексы списка котр  в []
"""



import random



def main():
    task_30_3()  
    task_32() 
    print("\n", "-"*12, "  END\n",  sep="")


def task_30_3():
    print("\n", "-"*12, "  Task30 \' progress \'", sep="")
    # strt,step,length=  [int (i) for i in input("Введите стартовый, шаг, длину:").strip().split(" ")]
    strt,step,length= 7,2,5
    print("Выведем заданую формулой an = a1 + (n-1) * d прогрессию\nc первым числом %d, шагом %d, длиной %d"%(strt, step, length))
    for i in range(length): 
       print((strt + (i) * step))


def task_30_2v():
    print("\n", "-"*12, "  Task30 \' progress \'", sep="")
    # strt,step,length=  [int (i) for i in input("Введите стартовый, шаг, длину:").strip().split(" ")]
    strt,step,length= 7,2,5
    for i in range(1,length+1): 
       print((strt + (i-1) * step))
   

def task_30():
    print("\n", "-"*12, "  Task30 \' progress \'", sep="")
    # strt,step,length=  [int (i) for i in input("Введите стартовый, шаг, длину:").strip().split(" ")]
    strt,step,length= 7,2,5
    recur_30(strt,step,length) 
   

def recur_30(strt,d,n):
    n-=1
    if n==0: 
        print(strt + (n) * d)
    else: 
        print(strt + (n) * d)
        return recur_30(strt,d,n)


def task_32():
   
   print("\n", "-"*12, "  Task32 \' indexes \'", sep="")
   
#    arrN1 = [random.randint(-8, 8) for z in range(-25,25)]
   arrN1 = [random.randint(-8, 8) for z in range(-5,5)]
   print("Есть масив:")
   print (arrN1) 
#    chL, chR = [int(i) for i in input("введите ограничения: лев и прав (два числа чз пробел)").strip().split(" ")]
   chL, chR = -4,4
   print("задаем диапазон от",chL,"до", chR)
   print("тотже список в диапазоне:")
   print([i    for i in arrN1   if   i>=chL and i<=chR ])
#    global cnt
#    cnt=0
   print("индексы первого списка с числами из диапазона:")
   print([ arrN1.index(i)  if   i>=chL and i<=chR else  'no'   for i in arrN1   ]    )
 

 


if __name__ == "__main__":
    main()




























