

'''  домашка
Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или ! фамилию, и Вы должны реализовать функционал
для изменения и удаления данных.
'''
 

import pathlib
from pathlib import Path
import random 
 

# path1=checkFileExst()
path1=Path(pathlib.Path.cwd(),"Hw08Files","phone_book_1.txt") 

                            

def main():
    pass

    
def checkFileExst():    
    # TODO перегрузить или лучше влюб случае -если файла нет выдать ответ - и там проверку чтобы дальше не выполнять др функции
    path2 = Path(pathlib.Path.cwd(),"Hw08Files","phone_book_1.txt")   
    try:
        with open(path2, "r") as f3:
            lines = f3.readlines()
            if len(lines)<1:
                print("Записей нет")  
            # else:              
            #     for linesL in lines:
            #         print(linesL.strip())
    except IOError:
        print("Файл сравочника еще не создан")
        print("Создаем файл..")
        with open(path2, "w") as f3:
            pass
        print("Файл создан. Записей нет")       
        print("Генерация справочника - пункт - 33 ")     

    return path2

def task_49_restore(strName):
    corTrue=False
    with open(path1, 'r+') as fRW:
        lines= fRW.readlines()
        for cnt,linesEn in enumerate(lines):
            if strName in linesEn:
                print(cnt,linesEn.strip())
                corTrue=True

    if corTrue:
        # TODO  проверка на число
        # TODO  проверка на числа в списке - ато удалит когото другого   
        inpCorNmbr= int(input("кого именно корректируем: - укажите показаный номер\n").strip())     
        # TODO проверка на ввод др значений                 
        impWht = input("Укажите что коректируем: 1-Имя 2-Фамилию 3-Номер телефона\n").strip()       
        impNewValue = input("Введите новое значение:\n").strip()

        print("было: ", lines[inpCorNmbr].strip())
        strMid = lines[inpCorNmbr].strip().split(" ")
        strMid[impWht-1]=impNewValue    
        strnew = strMid[0]+" "+strMid[1]+" "+strMid[2]+"\n"  
        print("стало:",strnew)

        lines[inpCorNmbr]= strnew 

        with open(path1, 'w') as fxWr:                            # перзаписываем файл начисто 
            fxWr.writelines(lines)
    else:
        print("Таких нет")

def task_49_del(strName):
    delTru= False
    # checkFileExst()                   
    with open(path1, 'r+') as fRW:
        lines= fRW.readlines()
        for cnt,linesEn in enumerate(lines):
            if strName in linesEn:
                print(cnt,linesEn.strip())
                delTru=True
      
    if delTru:
        # TODO проверка на числа в спсике- ато удалит когото другого
        inpD= int(input("кого именно удаляем- укажите показаный номер\n").strip())                      
        print("удаляем",lines[inpD].strip())
        # TODO можно удалить неск или всех
        del lines[inpD]                                 
        with open(path1, 'w') as fxWr:                  # перзаписываем файл начисто 
            fxWr.writelines(lines)
    else:
        print("Таких нет")



def task_49_print_all():
    try:
        with open(path1, "r") as f3:
            lines = f3.readlines()
            if len(lines)<1:
                print("Записей нет")  
            else:              
                for linesL in lines:
                    print(linesL.strip())

    except IOError:
        print("Сравочник еще не создан")
        with open(path1, "w") as f3:
            pass
        print("Сравочник создан. Записей нет")        

def task_49_add_cntcnt(strKntk): 
    with open(path1, 'a') as fW:
        fW.write(strKntk+"\n") 


def task_49_search_family(name):  
    with open(path1, "r") as f3:
        yep = False
        for cnt,lines in enumerate(f3):
            if name in lines:
                print("Вот похожий: ",cnt, lines.strip())     
                yep=True; 
        if yep!=True:
              print("Таких нет")  


#генр тлфн книги
def task_49_phnbk_genXXX(cntNew,path1): 
 
     
    strs="andrey23 79213400934"
    # last=strs.split() 

    names=["andrey","olga","sergey","mary","ira","uri","kirill","fantomas"]
    fmlNames=["nikit","zasmolin","ulyanov"]
    # dop=["coder","appraiser","gamer"]

    listNew= list([]) 

    for i in range(1,cntNew+1):
        fnbkNewName= random.choice(names)+str(int(1)+i)
       
        fnbkNewFmlyName= random.choice(fmlNames)+str(int(1)+i)

        nmbr = 7921_123_00_01 
        lastNm = int(1)
        fnbkNewNmbrTlf=str(nmbr+int(lastNm)+random.randint(1000,5000))

        # fnbkNewDop= random.choice(dop)

        listNewStr = [[fnbkNewName,fnbkNewFmlyName,fnbkNewNmbrTlf]]
        listNew  +=listNewStr

    [print(x) for x in listNew]
    


    with open(path1, 'a') as fA:
        for strs in listNew:
            for notes in strs:
                 fA.write(str(notes)+" ")            
            fA.write("\n")     



if __name__ == "__main__":
    main()


