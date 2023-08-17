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

y = melbourne_data.Price
print(y)

# Create the list of features below
feature_names = ["Rooms", "Price", "Bathroom", "Car", "YearBuilt"]

# Select data corresponding to features in feature_names
X = melbourne_data[feature_names]

# print description or statistics from X
print(X)

# print the top few lines
X.head()

from sklearn.tree import DecisionTreeRegressor

#For model reproducibility, set a numeric value for random_state when specifying the model
iowa_model = DecisionTreeRegressor(random_state=1)

# Fit the model
iowa_model.fit(X, y)

print("Making predictions..")
predictions = iowa_model.predict(X)
print(predictions)

#compare the top few predictions to the actual home values (in y) for those same homes
y.head()