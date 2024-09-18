
import pandas as pd

#reading the file of cars
cars = pd.read_csv('cars.csv')

#use the iloc function to look at the first 5 rows and the odd numbered columns
a = cars.iloc[:5,1::2]

#printing the first 5 rows and the odd numbered columns
print(a)

#using the loc function to specifically target the Mazda
b = cars.loc[cars['Model'] == 'Mazda RX4']

#print the row that contains the mazda rx4
print(b)

#also using loc function in which we can see the number of cylinders does the Camaro Z28 has

c = cars.loc[cars['Model'] == 'Camaro Z28', ['Model','cyl']]

#print the number of the camaro and how many cylonder it has
print(c)

#Making the code in which we can see the cyclinders and gears of the said cars
d = cars.loc[cars['Model'].isin(['Mazda RX4 Wag','Ford Pantera L', 'Honda Civic' ]),['Model','cyl','gear']]

# printing the wanted data for the given cars
print(d)


