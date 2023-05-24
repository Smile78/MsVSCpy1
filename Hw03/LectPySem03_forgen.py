'''
уникальных
значений в словаре.
Input: [
    {"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}
]
'''


# inp_dict ={"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}
inp_dict = {"V": "S001",  "V": "S002", "VI": "S001", "VI": "S005","VII": " S005 ", " V ": " S009 ", "VIII": " S007 "}
inp_dict2 = [{"V": "S001",  "V": "S002", "VI": "S001", "VI": "S005","VII": " S005 ", " V ": " S009 ", "VIII": " S007 "}, {"V2": "Sx001",  "V2": "Sx002", "VI2": "Sx001", "VI2": "Sx005" }]

#print("inp2 ",inp_dict2[0]) 

res = list(set(
    jstName 
    for dic in inp_dict2 
    for jstName in dic.values()))



print(res)

# print(type(inp_dict))

l = list()
l2 = list()

#print(inp_dict)

for v in inp_dict.values():
    l2.append(v)

#print(set(l2))

for k, v in inp_dict.items():
    # print(k)
    #print(v)
    l.append(v)
#print(l)
s = set(l)

#print(s)
