

""" Задача 34: Winnie the poh
"""

""" Задача 36: mult table
"""


 

def main():
    print("\n", "-"*12, "  START",  sep="")
    task_36_1(lambda x,y: x*y,6,6)
    task_36_1(lambda x,y: x+y,6,6)
    task_34_2()
    print("\n", "-"*12, "  END\n",  sep="")



def task_36_1(fncL,x,y):
    print("\n", "-"*12, "  Task36  \' table \'", sep="")
    for xC in range(1,x+1):
        for yC in range(1,y+1): 
            if yC==y: print(fncL(xC,yC), sep=' ', end='\n')         
            else: print(fncL(xC,yC), sep=' ', end=' ' )         


def task_34_2():
    print("\n", "-"*12, "  Task34  \' Winnie \'", sep="")

    txtSongRaw= 'пара-ра-рам рам-пам-папам па-ра-па-дам'
    txtSong = txtSongRaw.strip().split()

    aMas=list()

    for i in txtSong:
        aMas.append(len([x for x in i if x in ['а','ё']])) 
    
    if max(aMas)==min(aMas): print('Парам пам-пам')
    else: print('Пам парам')

 
def task_34_1():
    print("\n", "-"*12, "  Task34  \' Winnie \'", sep="")

    txtSongRaw= 'пара-ра-рам рам-пам-папам па-ра-па-дам'
    txtSong = txtSongRaw.strip().split(" ")

    aMas=list([int(0) for x in txtSong])
    
    for i,slovo in enumerate(txtSong):
        for c in slovo:
            if c in 'aеёыийэоюя': 
                if aMas[i]==0 or  int(aMas[i])!=aMas[i] : aMas[i]=1
                else: aMas[i]+=1
 
    if max(aMas)==min(aMas): print('Парам пам-пам')
    else: print('Пам парам')




if __name__ == "__main__":
    main()




























