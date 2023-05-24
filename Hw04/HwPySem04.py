'''
Задача 22: array
Задача 24: picking
'''


import os
import random


def main():
    # task_22_array()
    # task_22_array_2()
    task_24_picking()
    print("\n", "-"*12, "  END\n",  sep="")


def task_22_array_2():
    l1 = [random.randint(0, 20) for x in range(10)]
    l2 = [random.randint(0, 20) for x in range(10)]
    dimSet1 = set(sorted(l1))
    dimSet2 = set(sorted(l2))
    dimSet3 = (dimSet1 & dimSet2)
    print(dimSet3)


def task_22_array():
    print("\n", "-"*12, "  Task22 \' 2 arrays \'", sep="")
    # inp1qntarr1, inp1qntarr2 = [int(x) for x in list(input(
    # "Введите два числа чз пробел - это будут размеры двух массивов для сравнения:").strip().split(" "))]
    # dim1 = [random.randint(0, 20) for x in range(inp1qntarr1)]
    dim1 = [random.randint(0, 20) for x in range(10)]
    # dim2 = [random.randint(0, 20) for x in range(inp1qntarr2)]
    dim2 = [random.randint(0, 20) for x in range(10)]
    dimOut = [x for x in dim1 if x in dim2]
    dimOut.sort()
    setOut = set(dimOut)
    print(dim1)
    print(dim2)
    print("result \'like left join:\'",  str(setOut) if (
        len(setOut)) > 0 else "no simillar nambers")


def task_24_picking():
    print("\n", "-"*12, "  Task24 \' picking \'", sep="")
    kustQnt = random.randint(4, 14)
    print("lets assume that the household has orchard with round beds of %d bushes" % (kustQnt))
    dim_Berris_of1Bed = list([random.randint(1, 20) for x in range(kustQnt)])
    print("so, there is a quantity of berries on each bush accordinly:")
    txt2towrit = str(dim_Berris_of1Bed)

    file_Max_Strings = 5
    file_Max_Strings_Cnt = 0
    fileErase = bool(False)

    import pathlib
    from pathlib import Path 
    
   
 
    # path1txt= r"D:\MOE\Coding\GBedu\2RzrA2_Python_seminrs\Hw04\bed.txt"             //трабл экранирование ???
    # path1txt= "D:\\MOE\\Coding\\GBedu\\2RzrA2_Python_seminrs\\Hw04\\bed.txt"        //трабл правл послдевтл ???
    # path1txt= "D:\MOE\Coding\GBedu\2RzrA2_Python_seminrs\Hw04\bed.txt"              //трабл правл послдевтл ???
    # path1 = Path("MOE","Coding","GBedu","2RzrA2_Python_seminrs","Hw04","bed.txt")    //трабл
    path1 = Path(pathlib.Path.cwd(),"Hw04","bed.txt")                                   //ok

    print(path1)
   

    with open(path1, "a") as f21:
        print("пишу в файл:\n", " "*22, txt2towrit)
        f21.write(txt2towrit+"\n")

    with open(path1, "r") as f3:
        # txt1= f[len(f)].readline()
        for lines in f3:
            txtLast = str(lines)
    print("читаю из файла..")
    # print("прочел строку..",txtLast )
    txtLast = txtLast.replace("[", "")
    txtLast = txtLast.replace("]", "")
    txtLast = txtLast.replace(",", "")
    txtLast = txtLast.replace("\n", "")
    # print("прочел строку..", txtLast)
    txtLastDim = list(txtLast.split(" "))
    # print(txtLastDim)

    dim_Berris_of2Bed_readed = [int(x) for x in txtLastDim]
    print("мссв из прочтенного:\n", " "*22, dim_Berris_of2Bed_readed)
    # print(dim_Berris_of2Bed_readed)
    # maxSum3 = max((dim_Berris_of1Bed[0]+dim_Berris_of1Bed[1]+dim_Berris_of1Bed[2]), ((dim_Berris_of1Bed[len(dim_Berris_of1Bed)-2]+dim_Berris_of1Bed[len(
    #     dim_Berris_of1Bed)-1]+dim_Berris_of1Bed[0])), ((dim_Berris_of1Bed[len(dim_Berris_of1Bed)-1]+dim_Berris_of1Bed[0]+dim_Berris_of1Bed[1])))
    # for i in range(len(dim_Berris_of1Bed)-2):
    #     if dim_Berris_of1Bed[i]+dim_Berris_of1Bed[i+1]+dim_Berris_of1Bed[i+2] > maxSum3:
    #         maxSum3 = dim_Berris_of1Bed[i] + \
    #             dim_Berris_of1Bed[i+1]+dim_Berris_of1Bed[i+2]
    # print("so maxSum of berris =", maxSum3)

    massReds = list()
    for i in range(len(dim_Berris_of1Bed)-1):
        massReds.append(dim_Berris_of2Bed_readed[i-1]+dim_Berris_of2Bed_readed[i]+dim_Berris_of2Bed_readed[i+1])

    maxBeries=max(massReds) 
    print(maxBeries)

    with open(path1, "r") as f22:
        for xLines in f22:
            file_Max_Strings_Cnt = file_Max_Strings_Cnt+1
        #   print(xLines)
        # print("строк",file_Max_Strings_Cnt)
        if file_Max_Strings_Cnt >= file_Max_Strings:
            fileErase = True

    if fileErase:
        with open(path1, "w") as f1:
            # print("очистили файл")
            pass


if __name__ == "__main__":
    main()
