
import pandas as pd

# Load the .csv file into a DataFrame named cars
cars = pd.read_csv('cars.csv')
# Display the first five rows of the DataFrame
print(cars.head())

# Display the last five rows of the DataFrame
print(cars.tail())
