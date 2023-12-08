#Exercises: Level 1

#Day 2: 30 Days of python programming

first_name = "Dams"
last_name = "Gabriel"
full_name = "Bolu Ade"
country = "Nigeria"
city = "Kafanchan"
age = 28
year = 2023
is_married = "Yes"
is_true = "No"
is_light_on = "Bright"

first_name, last_name, full_name, country, city, age, year is_married, is_true, is_light_on  = 'Dams', 
'Gabriel', 'Bolu Ade', 'Nigeria', 'Kafanchan', 28, 2023, 'Yes', 'No', 'Bright'

#Exercises: Level 2

#Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

#Using the len() built-in function, find the length of your first name
print(len(first_name))
print(len(last_name))

#Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
reminder = num_two % num_one
exp = num_one ^ num_two
floor_division = num_one // num_two

#The radius of a circle is 30 meters
#Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = 3.14 * 30 ^2

#Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * 3.14 * 30 

#Take radius as user input and calculate the area.
area = 2 * 3.14 * 30

#Use the built-in input function to get first name, last name,
#country and age from a user and store the value to their corresponding variable names

first_name = input('What is your first name: ')
last_name = input('What is your last name: ')
country = input('What is your country: ')
age = input('How old are you? ')

print(first_name)
print(last_name)
print(country)
print(age)
