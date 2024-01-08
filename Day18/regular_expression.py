# Day 18: 30 days of Python programming
# Exercises: Day 18
# importing the re module for regular expressions
import re

# Exercises: Level 1

# What is the most frequent word in the following paragraph?
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
words = paragraph.replace('.','').split(' ')
dict = {}
for word in words:
    dict[word] = dict.get(word,0) + 1
sort_keysval = sorted(dict.items(),key = lambda x:x[1], reverse=True)
sort_keysval[0] # love occurs 6 times.

# The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.
# points = ['-12', '-4', '-3', '-1', '0', '4', '8']
# sorted_points =  [-12, -4, -3, -1, -1, 0, 2, 4, 8]
# distance = 8 -(-12) 
import re

# Given text containing the numbers
text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."

# Use regular expression to find all numbers in the text
numbers = re.findall(r'-?\d+', text)

# Convert the extracted numbers to integers
points = list(map(int, numbers))

# Sort the points in ascending order
sorted_points = sorted(points)

# Calculate the distance between the two furthest particles
distance = sorted_points[-1] - sorted_points[0]

print(f"The distance between the two furthest particles is: {distance}") #20

# Exercise Level 2
# Write a pattern which identifies if a string is a valid python variable

import re

def is_valid_variable(variable_name):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return bool(re.match(pattern, variable_name))

# Test cases
print(is_valid_variable('first_name'))   # Output: True
print(is_valid_variable('first-name'))   # Output: False
print(is_valid_variable('1first_name'))  # Output: False
print(is_valid_variable('firstname'))    # Output: True

# Exercise Level 3
# Clean the following text. After cleaning, count three most frequent words in the string.

# sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

# print(clean_text(sentence));
# I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
# print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]

import re
from collections import Counter

def clean_text(sentence):
    # Remove special characters, punctuation, and convert to lowercase
    cleaned_text = re.sub(r'[^A-Za-z\s]', '', sentence)
    cleaned_text = cleaned_text.lower()
    return cleaned_text

def most_frequent_words(cleaned_text):
    words = cleaned_text.split()
    word_count = Counter(words)
    return word_count.most_common(3)

# Given sentence
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

# Clean the text
cleaned_text = clean_text(sentence)
print(cleaned_text)

# Get the three most frequent words
result = most_frequent_words(cleaned_text)
print("The three most frequent words are:", result)