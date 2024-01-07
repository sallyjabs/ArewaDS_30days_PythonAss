# Day 9 of 30 Days of Python

# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. 
age = int(input("Enter your age: "))
if age >= 18: 
    print("You are old enough to drive.")
else:
    print(f"You need {18 - age} more years to learn to drive.")

# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age
my_age = 34
your_age = int(input("Enter your age: "))
if my_age > your_age:
    if my_age - your_age > 1:
        print(f"I am {my_age - your_age} years older than you.")
    else:
        print(f"I am {my_age - your_age} year older than you.")
elif your_age > my_age:
    if your_age - my_age > 1:
        print(f"You are {your_age - my_age} years older than me.")
    else:
        print(f"You are {your_age - my_age} year older than me.")
else:
    print("We are age mates!")

# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.
a = input("Enter number one: ")
b = input("Enter number two: ")
if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")

'''Write a code which gives grade to students according to theirs scores:

80-100, A
70-89, B
60-69, C
50-59, D
0-49, F'''

# Accept the score through user input
stu_score = input("Enter your score: ")
try:
    score = int(stu_score)
    # Assign grades based on score
    if score > 100:
        print("Score cannot be greater than 100")
    elif score >= 80:
        print("You have an A")
    elif score >= 70:
        print("You have a B")
    elif score >= 60:
        print('You have a C')
    elif score >= 50:
        print("You have a D")
    elif score > 0:
        print("You have an F")
    else:
        print("Please enter a valid score starting from 0 to 100")

except ValueError:
    print("Please enter a valid score")

# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

month = input("Enter the month you wish to check its season: ")
seasons = {"autumn":["September","October","November"], 
            "winter":["December","January","February"],
            "spring":["March","April","May"],
            "summer":["June","July","August"]}
if month.title() in seasons["autumn"]:
    print(f"The season for the month of {month} Autumn")
elif month.title() in seasons["winter"]:
    print(f"The seaon for the month of {month} is Winter")
elif month.title() in seasons["spring"]:
    print(f"The seaon for the month of {month} is Spring")
elif month.title() in seasons["summer"]:
    print(f"The seaon for the month of {month} is Summer")
else:
    print("Please enter a correct month.")

# The following list contains some fruits:

fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

input_fruits = input("Enter a fruit name to add: ")
if input_fruits in fruits:
    print("That fruit already exist in the list.")
else: 
    fruits.append(input_fruits)
    print(f"{input_fruits} added to list successfully", fruits)

# Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Tolu',
    'last_name': 'Ola',
    'age': 34,
    'country': 'Nigeria',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '80000'
    }
}

#  Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if "skills" in person:
    print(person["skills"][2])

#  Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if "skills" in person:
    if "Python" in person["skills"]:
        print("The person has python skills")
    else:
        print("This person does not have python skills.")

#  If the person is married and if he lives in Finland, print the information in the following format:
# Asabeneh Yetayeh lives in Finland. He is married.
if person["is_marred"] is True:
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']} and he is married")
else:
    print("He is single")