
 
import tlfn_func_Last_HW as f1
import tlfn_intrfc_ok_HW as intrf1

inp=int()

while inp!=6:                                   # завершение / номер стоп
    inp = intrf1.interface1()
    f1.checkFileExst() 
    match inp :
        case 1:
            f1.task_49_print_all()
        case 2:
            name,faml,tlfn=input("введите имя и фамилию и цифры\n").strip().split() 
            f1.task_49_add_cntcnt(name+" "+faml+" "+tlfn)
        case 3: 
            name=input("введите имя\n").strip() 
            f1.task_49_search_family(name) 
        case 4:
            name=input("введите имя для корректировки\n").strip() 
            f1.task_49_restore(name)        
        case 5: 
            name=input("введите имя\n").strip() 
            f1.task_49_del(name)
        case 6: pass  
        case 33: 
            f1.task_49_phnbk_genXXX(13,f1.path1)  
            # f1.task_49_print_all()
        case _: print("input error")    
print("До новых встреч")
    


   