# importing the module
import pandas as pd
import math
import re
class_file = "C:\\Users\\Tyler\\source\\repos\\Web Scraper\\Web Scraper\\class_file.txt"
# read specific columns of csv file using Pandas
df = pd.read_csv("food.csv", usecols=['Name', 'Weight', 'Value', 'Hardcore mode effects'])
name_list = df['Name'].tolist()
weight_list = df['Weight'].tolist()
value_list = df['Value'].tolist()
hunger_list = df['Hardcore mode effects'].tolist()

sell_list = []
for i in value_list:
    price = i / 3
    sell_list.append(price)

class_list = []
for i in name_list:
    j = i.replace("'","")
    o = j.replace(' &', '').lower()
    k = o.replace(' ','_')
    l = k.replace('-','_')
    class_list.append(l)

icon_list = []

for i in class_list:
    j =''.join(('ico_' , i)).lower()
    icon_list.append(j)

final_hunger_list = []
l = 0 
for i in hunger_list:
    l += 1
    o = str(hunger_list[l-1]).split('FOD')[0]
    p = o.replace("-"," ")
    k = p.replace(" ","")
    try:
        int(k)
    except:
        k = -1
    final_hunger_list.append(k)

p = 0

print(class_list)
open(class_file, "w").close()
for i in class_list:
    p +=1
    with open(class_file, 'a') as file:
        file.write(f"    class {i}" + " {\n")
        file.write(f'        variable = "{i}";\n')
        file.write(f'        displayName = "STR_Item_{i}";\n')
        file.write(f'        weight = {weight_list[p-1]};\n')
        file.write(f'        buyPrice = {value_list[p-1]};\n')
        file.write(f'        sellPrice = {math.ceil(sell_list[p-1])};\n')
        file.write(f'        illegal = false;\n')
        file.write(f'        edible = -1;\n')
        file.write(f'        drinkable = -1;\n')
        file.write(f'        icon = "icons\\{icon_list[p-1]}.paa";\n')
        file.write("    };\n\n")
#    class name {
#        variable = "name";
#        displayName = "STR_Item_name";
#        weight = 1;
#        buyPrice = 65;
#        sellPrice = 50;
#        illegal = false;
#        edible = 10;
#        drinkable = -1;
#        icon = "icons\\ico_apple.paa";
#    };

    