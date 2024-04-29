import pandas as pd

url = 'https://fallout.fandom.com/wiki/Fallout:_New_Vegas_miscellaneous_items'
all_tables = pd.read_html(url)


# getting the required table from list
population_table = all_tables[5]
# saving CSV in the current working directory
population_table.to_csv('misc.csv', index=False)