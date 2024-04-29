# import required module
import pandas as pd
import os
from PIL import Image
# assign directory
directory = 'C:\\Users\\Tyler\\source\\repos\\Web Scraper\\Web Scraper\\New Vegas Food'

# read specific columns of csv file using Pandas
df = pd.read_csv("food.csv", usecols=['Name'])
list = df['Name'].tolist()
new_list = []
for i in list:
    j = i.replace(' ','_')
    new_list.append(j)

final_list = []

for i in new_list:
    j =''.join(('ico_' , i)).lower()
    final_list.append(j)
    
# iterate over files in
# that directory
i = 0    
for filename in  sorted(os.listdir(directory), key=len):
    f = os.path.join(directory, filename)
    # Resizing File
    i += 1
    im=Image.open(f)
    im = im.resize((64,64), resample=Image.NEAREST)
    im.save(f'{final_list[i-1]}.png')