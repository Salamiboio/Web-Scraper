# importing the module
import pandas as pd
import math
import re
string_file = "C:\\Users\\Tyler\\source\\repos\\Web Scraper\\Web Scraper\\string_file.txt"
# read specific columns of csv file using Pandas
df = pd.read_csv("food.csv", usecols=['Name'])
name_list = df['Name'].tolist()
class_list = []
for i in name_list:
    j = i.replace("'","")
    k = j.replace(' ','_').lower()
    class_list.append(k)
open(string_file, "w").close()
p = 0
for i in class_list:
    p +=1
    with open(string_file, 'a') as file:
        
        file.write(f'        <Key ID="STR_Item_{class_list[p-1]}">\n')
        file.write(f'           <Original>{name_list[p-1]}</Original>\n')
        file.write(f'           <Czech>{name_list[p-1]}</Czech>\n')
        file.write(f'           <Spanish>{name_list[p-1]}</Spanish>\n')
        file.write(f'           <Russian>{name_list[p-1]}</Russian>\n')
        file.write(f'           <German>{name_list[p-1]}</German>\n')
        file.write(f'           <French>{name_list[p-1]}</French>\n')
        file.write(f'           <Italian>{name_list[p-1]}</Italian>\n')
        file.write(f'           <Portuguese>{name_list[p-1]}</Portuguese>\n')
        file.write(f'           <Polish>{name_list[p-1]}</Polish>\n')
        file.write(f'           <Chinesesimp>{name_list[p-1]}</Chinesesimp>\n')
        file.write(f'       </Key>\n')
        

        
#        <Key ID="STR_Item_Apple">
#            <Original>Apple</Original>
#            <Czech>Jablko</Czech>
#            <Spanish>Manzana</Spanish>
#            <Russian></Russian>
#            <German>Apfel</German>
#            <French>Pomme</French>
#            <Italian>Mela</Italian>
#            <Portuguese>Maçã</Portuguese>
#            <Polish>Jabłko</Polish>
#			<Chinesesimp>苹果</Chinesesimp>
#        </Key>