# Day 4 for 30 Days of learning Python

#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
string_1 = 'Thirty'
string_2 = 'Days'
string_3 = 'Of'
string_4 = 'Python'
space = ' '
conca_string = string_1 + ' ' + string_2 + ' ' + string_3 + ' ' + string_4
print(conca_string)

#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
string_1 = 'Coding'
string_2 = 'For'
string_3 = 'All'

conca_all = string_1 + ' ' + string_2 + ' ' + string_3
print(conca_all)

#Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

#Print the variable company using print().
print(company)

#Print the length of the company string using len() method and print()
print(len(company))

#Change all the characters to uppercase letters using upper() method
print(len(company.upper()))

#Change all the characters to lowercase letters using lower() method
print(len(company.lower()))

#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All
print(company.capitalize())
print(company.title())
print(company.swapcase())

#Cut(slice) out the first word of Coding For All string
string_1 = 'Coding For All'
first_word = string_1[0]
print(first_word)

#Check if Coding For All string contains a word Coding using the method index, find or other methods
print('Coding' in 'Coding For All')

#Replace the word coding in the string 'Coding For All' to Python
string = 'Coding For All'
action = string.replace('Coding', 'Python')
print(action)

#Change Python for Everyone to Python for All using the replace method or other methods
string = 'Python For Everyone'
action = string.replace('Everyone', 'All')
print(action)

#Split the string 'Coding For All' using space as the separator (split())
string = 'Coding For All'
split_string = string.split(' ')
print(split_string)

#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma
social_platform = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
split_platforms = social_platform.split(',')
print(split_platforms)

#What is the character at index 0 in the string Coding For All
string = 'Coding For All'
action = string[0]
print(action)

#What is the last index of the string Coding For All
string = 'Coding For All'
action = string[-1]
print(action)

#What character is at index 10 in "Coding For All" string
string = 'Coding For All'
action = string[10]
print(action)

#Create an acronym or an abbreviation for the name 'Python For Everyone'
acronym = 'Python For Everyone'
abbrev = acronym[0:7:11]
print(abbrev)

#Create an acronym or an abbreviation for the name 'Coding For All
acronym = 'Coding For All'
abbrev = acronym[0:8:12]
print(abbrev)

#Use index to determine the position of the first occurrence of C in Coding For All
string = 'Coding For All'
first_position = string.index('C')
print(first_position)

#Use index to determine the position of the first occurrence of F in Coding For All
string = 'Coding For All'
first_position = string.index('F')
print(first_position)

#Use rfind to determine the position of the last occurrence of l in Coding For All People
string = 'Coding For All'
last_position = string.rfind('l')-1
print(last_position)

#Use index or find to find the position of the first occurrence of the word 'because' in the 
#following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentense = 'You cannot end a sentence with because because because is a conjunction'
print(sentense.index('because'))

#Use rindex to find the position of the last occurrence of the word because in the
# following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentense = 'You cannot end a sentence with because because because is a conjunction'
sub_string = 'because'
print(sentense.rindex(sub_string))

#Slice out the phrase 'because because because' in the
#following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentense = 'You cannot end a sentence with because because because is a conjunction'
slice_phrase = sentense[30:55]
print(slice_phrase)

#Does ''Coding For All' start with a substring Coding?
string = 'Coding For All'
sub_string = 'Coding'
action = string.startswith(sub_string)
print(action)

## Does 'Coding For All' end with a substring coding?
string = 'Coding For All'
sub_string = 'coding'
action = string.endswith(sub_string)
print(action)

#Coding For All      '  , remove the left and right trailing spaces in the given string
string = '   Coding For All      '
print(string.strip())

#Which one of the following variables return True when we use the method isidentifier():
#30DaysOfPython
#thirty_days_of_python
challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True

#The following list contains the names of some of python libraries:
# ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
combo_lib = ' '.join(python_libraries)
print(combo_lib)

#Use the new line escape sequence to separate the following sentences
string = 'I am enjoying this challenge. \nI just wonder what is next.'
print(string)

#Use a tab escape sequence to write the following lines.
string = 'Name \t\tAge \tCountry \tCity \nAsabeneh \t250 \tFinland \tHelsinki'
print(string)

#Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area}")

#Make the following using string formatting methods:
## 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
a = 8
b = 6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))
