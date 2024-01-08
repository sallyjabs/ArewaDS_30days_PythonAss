# Day 12: 30 days of python programming
# Write a function which generates a six digit/character random_user_id.
#   print(random_user_id());

import random
import string
def random_user_id():
    return "".join(str(random.choice(string.ascii_letters + string.digits)) for i in range(6))

print(random_user_id()) 

# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
# print(user_id_gen_by_user()) # user input: 5 5
#output:
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf
   
# print(user_id_gen_by_user()) # 16 5
#1GCSgPLMaBAVQZ26
#YD7eFwNQKNs7qXaT
#ycArC5yrRupyG00S
#UbGxOFI7UXSWAyKN
#dIV0SSUTgAdKwStr

def user_id_gen_by_user():
    try:
        # Get user input for number of characters and number of IDs
        char_count, id_count = map(int, input("Enter number of characters and number of IDs (separated by space): ").split())
        
        # Define the characters to choose from for the random ID
        characters = string.ascii_letters + string.digits  # letters (uppercase and lowercase) and digits
        
        # Generate user-specified number of IDs each with specified number of characters
        for _ in range(id_count):
            user_id = ''.join(random.choices(characters, k=char_count))
            print(user_id)
    except ValueError:
        print("Please enter valid numbers for characters and IDs.")


# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

def list_of_rgb_colors(num_colors):
    colors = []
    for _ in range(num_colors):
        # Generate random values for RGB components (0-255)
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        
        # Append the RGB tuple to the colors list
        colors.append((red, green, blue))
    
    return colors

# Generate a list of 5 RGB colors
num_of_colors = 5
rgb_colors = list_of_rgb_colors(num_of_colors)
print(rgb_colors)

# Write a function generate_colors which can generate any number of hexa or rgb colors.
# generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
# generate_colors('hexa', 1) # ['#b334ef']
# generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
# generate_colors('rgb', 1)  # ['rgb(33,79, 176)']


def rgb_color_gen():
    a = ','.join(str(random.randint(0,255)) for i in range(3))
    return 'rgb('+ a + ')'
print(rgb_color_gen())

# Exercises: Level 2
# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors(x):
     a= ["".join(str(random.choice('abcdef' + string.digits)) for i in range(6)) for j in range(x)]
     b =['#' + item for item in a]
     return b
list_of_hexa_colors(6)
# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

def list_of_rgb_colors(x):
    return [rgb_color_gen() for i in range(x)]

list_of_rgb_colors(7)

string.digits

# Write a function generate_colors which can generate any number of hexa or rgb colors.

def generate_colors(fun,x):
    if fun == 'hexa':
        result = list_of_hexa_colors(x)
    elif fun == 'rgb':
        result = list_of_rgb_colors(x)

    return result

generate_colors('hexa',3)
generate_colors('rgb',1)

# Exercises: Level 3
# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list

def shuffle_list(list):
    random.shuffle(list)
    return list
print(shuffle_list([1,2,3,4,5]))
    
# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def unique_random_nums():
    return random.sample([0,1,2,3,4,5,6,7,8,9],k=7)
print(unique_random_nums())
