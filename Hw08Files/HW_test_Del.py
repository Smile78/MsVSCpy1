
from pathlib import Path
import pathlib


path1= Path(pathlib.Path.cwd(),"Hw08Files","phnbkClean.txt")  

# with open(path1, 'r+') as fRW:
#     fRW.write('olga 45656'+"\n")
#     for lines in fRW:
#         print(lines.strip())
#         if 'dsmgfm' in lines:
#             fRW.write("x"+"\n")


with open(path1, "r") as file:
    lines = file.readlines()
    print(lines.index("dsmgfm 3462\n"))

# with open(path1, "r") as file:
#     lines = file.readlines()
# del lines[1]
# with open(path1, "w") as file:
#     file.writelines(lines)



