import pandas as pd

# save filepath to variable for easier access
melbourne_file_path = '~/Downloads/melb_data.csv'
# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path) 
# print a summary of the data in Melbourne data
melbourne_data.describe()

avg_lot_size = 558
newest_home_age = 2023 - 2018

print("average lot size: ",avg_lot_size)
print("newest home age: ",newest_home_age)

melbourne_data.columns
