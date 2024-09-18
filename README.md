# ECE21112-PA3

### PANDAS
#### Pandas is a Python library used for working with data sets. It has functions for analyzing, cleaning, exploring, and manipulating data.


### INTENDED LEARNING OUTCOMES
#### -To identify the codes and functions incorporated in the Pandas library
#### -To be able to apply and use the different codes and functions in creating a Python program using a
Pandas library


## PROBLEM 1
![image](https://github.com/user-attachments/assets/9f09c643-b595-4724-8f5e-4762b70d3090)


### OBJECTIVES FOR THIS PROBLEM

##### LOAD THE CSV FILE PROVIDED
##### PRINT THE FIRST AND LAST 5 ROWS OF THE CARS

### THE CODE:

#### ![image](https://github.com/user-attachments/assets/20cb7ff0-d63a-47f5-881c-82b6bbd4d69b)
#### ![image](https://github.com/user-attachments/assets/2ef90094-e1f0-45fa-9865-bbca0fb81b79)
#### ![image](https://github.com/user-attachments/assets/99ad521d-b3ef-411e-9fe9-81b49dd8986e)
#### ![image](https://github.com/user-attachments/assets/d69b5e35-6c29-4c63-9ec1-b8914cf96382)


### EXPLAINING THE CODES:

#### 1. cars = pd.read_csv('cars.csv') this line of code reads the given csv file that will be incorporated
#### 2. "cars.head()" this code outputs the first 5 row of the file 
#### OUTPUT : 
#### ![image](https://github.com/user-attachments/assets/69d6931e-82fa-41d4-ba53-fa6555af0d09)
#### 3. "cars.tail()" prints the last 5 rows of the file
#### OUTPUT: 
#### ![image](https://github.com/user-attachments/assets/26a57351-8435-48a9-8bce-1ea39e74b171)
#### 4. is to create a .py file using the write function.


## PROBLEM 2
#### ![image](https://github.com/user-attachments/assets/fc4a203c-2aa6-4bc6-b6e9-2e0727a83b52)


### OBJECTIVES FOR THIS PROBLEM

##### DISPLAT THE FIRST 5 ODD NUMBERED ROWS OF CARS
##### PRINT THE ROW OF THE SPECIFIC CAR (MAZDA RX4)
#### DISPLAY HOW MANY CYLINDERS THE CAMARO Z28 HAS
#### GET BOTH THE CYLINDER NUMBERS and GEAR TYPE  FOR THE CARS 'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic'.

### THE CODE: 

#### ![image](https://github.com/user-attachments/assets/aa89dde7-d413-49b2-924b-e6474a21769f)
#### ![image](https://github.com/user-attachments/assets/5fcd4798-b4e3-4be3-9acb-78d16ca59e11)
#### ![image](https://github.com/user-attachments/assets/3d6cc9f1-8335-4a4f-8aab-59acb443486f)
#### ![image](https://github.com/user-attachments/assets/9c92f51c-42d8-4929-a68b-bc31751fa153)
#### ![image](https://github.com/user-attachments/assets/b5c2f48a-f6fd-4e15-ab15-82a371604c54)
#### ![image](https://github.com/user-attachments/assets/99769c3a-2d48-41ae-aea2-8db7f1ba40fa)


### EXPLAINING THE CODES:

#### 1. cars = pd.read_csv('cars.csv') this line of code reads the given csv file that will be incorporated
#### 2. "cars.iloc[:5,1::2]" this is for to locate the first 5 rows and the od numbered columns
#### OUTPUT : ![image](https://github.com/user-attachments/assets/c367fb72-6e6b-457a-9b68-695abcea36c0)

#### 3. "cars.loc[cars['Model'] == 'Mazda RX4'" locates the specific row for the car given.
#### OUTPUT: ![image](https://github.com/user-attachments/assets/e6d7e17a-ad48-4b4a-9fc4-4d56eab5fbe4)
#### 4. "cars.loc[cars['Model'] == 'Camaro Z28', ['Model','cyl']] " This code filters the DataFrame cars to select rows where the Model column is 'Camaro Z28', and then it retrieves only the Model and cyl (cylinders) columns for those rows.
#### OUTPUT: 
#### ![image](https://github.com/user-attachments/assets/73cad6b0-f2a7-42ee-83bc-fd4ad4cf87c4)
#### 5. is to create a .py file using the write function.

### Author: PAOLO D. MENDOZA











