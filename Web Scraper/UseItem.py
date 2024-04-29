import pandas as pd
import math
import re
class_file = "C:\\Users\\Tyler\\source\\repos\\Web Scraper\\Web Scraper\\useitem_file.txt"
# read specific columns of csv file using Pandas
df = pd.read_csv("food.csv", usecols=['Name', 'Weight', 'Value', 'Effect', 'Hardcore mode effects'])
name_list = df['Name'].tolist()
weight_list = df['Weight'].tolist()
value_list = df['Value'].tolist()
effect_list = df['Effect'].tolist()
hunger_list = df['Hardcore mode effects'].tolist()

class_list = []
for i in name_list:
    j = i.replace("'","")
    o = j.replace(' &', '').lower()
    k = o.replace(' ','_')
    l = k.replace('-','_')
    class_list.append(l)
    
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
        k = 0
    final_hunger_list.append(k)
    
final_thirst_list = []
l = 0 
for i in hunger_list:
    l += 1
    o = str(hunger_list[l-1]).split('H2O')[0]
    p = o.split('FOD,')[-1]
    k = p.replace(" ","")
    g = k.replace("-","")
    try:
        int(g)
       
    except:
        g = 0
    final_thirst_list.append(g)

hp_list = []
k = 0
for i in effect_list:
    k += 1
    o = str(effect_list[k-1]).split('HP')[0]
    p = o.replace("+","")
    n = p.replace("-","")
    try:
        int(n)
        hp_list.append(o)
    except:
        o = "+0"
        hp_list.append(o)

time_list = []
k = 0
for i in effect_list:
    k += 1
    j = effect_list[k-1].split("max HP")[0]
    h = j.split('Max HP')[0]
    o = h.split("s)")[0]
    p = o.split("HP (")[-1]
    try:
        int(p)
        time_list.append(p)
    except:
        p = 0
        time_list.append(p)
    
rad_list = []
k = 0
for i in effect_list:
    k += 1
    o = effect_list[k-1].split("),")[-1]
    l = o.split("HP,")[-1]
    p = l.split('RAD')[0]
    j = p.replace("+","")
    h = j.replace(" ","")
    try:
        int(h)
        rad_list.append(h)
    except:
        h = 0
        rad_list.append(h)
    
st_list = []
k = 0
for i in effect_list:
    k += 1
    o = effect_list[k-1].split("),")[-1]
    l = o.split("HP,")[-1]
    p = l.split("RAD,")[-1]
    j = p.split("ST")[0]
    g = j.replace("+","")
    h = g.replace(" ","")
    try:
        int(h)
        st_list.append(h)
    except:
        h = 0
        st_list.append(h)

pe_list = []
k = 0
for i in effect_list:
    k += 1
    o = effect_list[k-1].split("),")[-1]
    l = o.split("HP,")[-1]
    p = l.split("RAD,")[-1]
    j = p.split("PE")[0]
    g = j.replace("+","")
    h = g.replace(" ","")
    try:
        int(h)
        pe_list.append(h)
    except:
        h = 0
        pe_list.append(h)
    
en_list = []
k = 0
for i in effect_list:
    k += 1
    o = effect_list[k-1].split("),")[-1]
    l = o.split("HP,")[-1]
    p = l.split("RAD,")[-1]
    j = p.split("EN")[0]
    g = j.replace("+","")
    h = g.replace(" ","")
    try:
        int(h)
        en_list.append(h)
    except:
        h = 0
        en_list.append(h)

ch_list = []
k = 0
for i in effect_list:
    k += 1
    o = effect_list[k-1].split("),")[-1]
    l = o.split("HP,")[-1]
    p = l.split("RAD,")[-1]
    j = p.split("CH")[0]
    g = j.replace("+","")
    h = g.replace(" ","")
    try:
        int(h)
        ch_list.append(h)
    except:
        h = 0
        ch_list.append(h)
        
ch_list = []
k = 0
for i in effect_list:
    k += 1
    o = effect_list[k-1].split("),")[-1]
    l = o.split("HP,")[-1]
    p = l.split("RAD,")[-1]
    j = p.split("CH")[0]
    g = j.replace("+","")
    h = g.replace(" ","")
    try:
        int(h)
        ch_list.append(h)
    except:
        h = 0
        ch_list.append(h)

in_list = []
k = 0
for i in effect_list:
    k += 1
    o = effect_list[k-1].split("),")[-1]
    l = o.split("HP,")[-1]
    p = l.split("RAD,")[-1]
    j = p.split("IN")[0]
    g = j.replace("+","")
    h = g.replace(" ","")
    try:
        int(h)
        in_list.append(h)
    except:
        h = 0
        in_list.append(h)
   
ag_list = []
k = 0
for i in effect_list:
    k += 1
    o = effect_list[k-1].split("),")[-1]
    l = o.split("HP,")[-1]
    p = l.split("RAD,")[-1]
    j = p.split("AG")[0]
    g = j.replace("+","")
    h = g.replace(" ","")
    try:
        int(h)
        ag_list.append(h)
    except:
        h = 0
        ag_list.append(h)


for i in final_thirst_list:
    print(i)

p = 0
open(class_file, "w").close()
for i in class_list:
    with open(class_file, 'a') as file:
         file.write(f'    case "{i}": ' + "{\n")
         file.write(f'        if ([false, _item, 1] call life_fnc_handleInv) then' + " {\n")
         file.write(f'            [{hp_list[p]}, {time_list[p]}, "Chewy1", {final_hunger_list[p]}, {final_thirst_list[p]}, {rad_list[p]}, {st_list[p]}, {pe_list[p]}, {en_list[p]}, {ch_list[p]}, {in_list[p]}, {ag_list[p]}, 0, 120] spawn sal_fnc_useitem;\n')
         file.write("             closedialog 0;\n")
         file.write("         };\n")
         file.write("     };\n\n")
    p +=1








#        case "ant_meat": {
#            if ([false, _item, 1] call life_fnc_handleInv) then {
#                [Total_Healing, Time, "Sound", Hunger, Thirst, Rads, Strength, Perception, Endurance, Charisma, Intelligence, Agility, Luck, TimeSpecialsIsEffected] spawn sal_fnc_useitem;
#                closedialog 0;
#        };