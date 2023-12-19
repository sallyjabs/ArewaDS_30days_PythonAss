#Declare your age as integer variable, height as a float variable, and variable that store a complex number

age = 41
height = 8.2
comp = 1 +2j

#Write a script that prompts the user to enter base
#and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

base = input('enter base of triangle: ')
height = input('enter height of triangle: ')
area = 0.5 * base * height
print(area)

#Script to Calculate the perimeter of the triangle (perimeter = a + b + c).

a = input('enter side 5: ')
b = input('enter side 4: ')
c = input('enter side 3: ')

perimeter = a + b + c
print(perimeter)

#Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

length = input('enter length: ')
width = input('enter width: ')
area = length * width
perimeter = 2 * (length + width)

print(area, perimeter)

#Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

r = input('enter r: ')
pi = input('enter 3.14: ')
area = 3.14 * r * r
circumference = 2 * 3.14 * r
print(circumference)

#Calculate the slope, x-intercept and y-intercept of y = 2x -2

intercept_x = input('enter x-intercept (-1,0): ')
intercept_y = input('enter y-intercept (0,-2): ')
slope1 = 2 * (-1,0) - 2
print(slope1)

#Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1 = 2
x2 = 6
y1 = 2
y2 = 10
slope2 = y2-y1 / x2-x1

print(slope2)

#Compare the slopes in tasks 8 and 9

print(slope1 > slope2)
print(slope1 < slope2)
print(slope1 == slope2)
print(slope1 != slope2)

#Calculate the value of y (y = x^2 + 6x + 9)
x = 0
y = x^2 + 6*x + 9*x

#Find the length of 'python' and 'dragon' and make a falsy comparison statement
print(len("python"))
print(len("dragon"))
print(len("python") != len("dragon"))
print(len("python") > len("dragon"))

#Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')

#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('jargon' in 'I hope this course is not full of jargon')

#There is no 'on' in both dragon and python
print('on' not in 'python' and 'dragon')

#Find the length of the text python and convert the value to float and convert it to string
print(str(float(len('python'))))
print(float(len('python')))

#Even numbers are divisible by 2 and the remainder is zero.
# How do you check if a number is even or not using python?

num = int(input("Enter a number: "))
print("Number entered is even: ", (num % 2) < 1)

# Check floor division
print("Result is:", 7 // 3 == int(2.7))

#Check if type of '10' is equal to type of 10
print("type of 10 is:", type('10') == type(10))

#Check if int('9.8') is equal to 10
num = int(9.8) == 10
print(num)

#Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

hours = int(input("Enter number of hours: "))
rate_per_hr = float(input("Enter rate per hour: "))
weekly_earnings = hours * rate_per_hr
print(weekly_earnings)

#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. 

years_lived = int(input("Enter the number of years:"))
seconds_lived = years_lived * 12
print(seconds_lived)

#Write a Python script that displays the following table