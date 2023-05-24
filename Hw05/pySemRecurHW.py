

''' Задача 26:   возв в степень
Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.
A = 3; B = 5 -> 243 (3?)
A = 2; B = 3 -> 8
'''

''' Задача 28:   сумм 2х чисел ++
Напишите рекурсивную функцию 
sum(a, b),
возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.
'''

''' Задача xx:  треугольное число

'''


def main():
    # task_26_pow(2,2)
    task_26_pow(3,5)
    task_28_sum()
    task_xx_triangl(4)
    print("\n", "-"*12,"  END\n",  sep="") 



def task_xx_triangl(b):
    print("\n", "-"*12, "  Task_хх \' триангл \'", sep="") 
    print(recur_xx(b))

def recur_xx(b):
    if b==1: return 1
    else:
        return b+recur_xx(b-1)
    


def task_26_pow(b,p):
    print("\n", "-"*12, "  Task26 \' pow pow \'", sep="")    
    # recur_26_1(b,p,0,1)
    print(recur_26_2(b,p))

def recur_26_2(b,p):
    p-=1
    if p==1: return b*b
    else: 
        return recur_26_2(b,p)*b

def recur_26_1(b,p,p2,sum):
    if p2<p:
        p2+=1
        sum=sum*b
        recur_26_2(b,p,p2,sum)
    else:
        print(sum)



def task_28_sum():
    print("\n", "-"*12, "  Task28 \' recur sum \'", sep="")
    # recurN_28(3,2,0) 
    print(recur_28_3(3,2))
     
def recur_28_3(x,y):
    if y==0: return x
    else:
        return recur_28_3(x,y-1)+1

def recur_28_2(x,y):
    # global c = (int)1 
    if(y==0): print(x)
    else: 
        x+=1
        y-=1
        recur_28_2(x,y)

def recur_28_1(a,b,kolPls):
    if b>kolPls:
       kolPls+=1
       a+=1
       recur_28_1(a,b,kolPls)
    else:
       print(a)
        
 


if __name__ == "__main__":
    main()



