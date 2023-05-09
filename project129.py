import csv
import pandas as pd

with open('Dwarf_Stars.csv') as f:
    data = csv.reader(f)
    data_list = list(data)

m = data_list.pop(3)
r = data_list.pop(4)

star_name = data_list[1:]

headers = ['','star_name','distance','mass','radius']
# print(star_name)

for i in star_name:
    new_s = i[3]
    if new_s.isdigit():
        mas = float(new_s)*0.102763
    else:
        mas = ''
data_list.append(mas)

for i in star_name:
    new_s = i[4]
    if new_s.isdigit():
        rad = float(new_s)*0.000954588
    else:
        rad = ''
data_list.append(rad)

data_list.pop(0)

for i, v in enumerate(data_list):
    if v == ' ':
        del data_list[i]

with open('project130output(3).csv','w',encoding='utf8') as f:
    data1 = csv.writer(f)
    data1.writerow(headers)
    data1.writerows(data_list)