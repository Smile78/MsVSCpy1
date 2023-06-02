

def interface1():
    print('----- das ist Py file terminal -----')
    print('Доступны операции:\n1 - Вывод всех контактов \n2 - Добавление контакта \n3 - Поиск по контактам \n4 - Изменить данные контакта \n5 - Удалить контакт \n6 - Завершение работы\n----- ----- -----', sep="")

    # inp=int()
    # x=int()
   
    spin=True
 
    while spin>False:
        try:
            inp = int(input('Enter the number (1-6):\n'))
            # break
            x = inp 
            spin=False
        except ValueError:
            print('Error. Need to enter the number')
            spin=True
            # continue

         
    return x        
            
