# Day 8 of 30 days of python

# Create an empty dictionary called dog
empty_dict = {}

# Add name, color, breed, legs, age to the dog dictionary
dog = {"name":"max", "color":"black","breed":"sholio","legs":"german","age":5}
print(dog)

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
stu_dict = {"first_name": "Caleb", "last_name":"Joshua", "gender":"male","age":25, "marital status":"married","skills":["javascript","c_sharp","python","php"], "city":"kaduna","address":"Mountain Road, Kudenda"}

# Get the length of the student dictionary
print(len(stu_dict))

# Get the value of skills and check the data type, it should be a list
print(stu_dict["skills"])

# Modify the skills values by adding one or two skills
stu_dict["skills"].append("laravel")
print(stu_dict["skills"])

# Get the dictionary keys as a list
keys = stu_dict.keys()
print(keys)

# Get the dictionary values as a list
values = stu_dict.values()
print(values)

# Change the dictionary to a list of tuples using items() method
print(stu_dict.items())

# Delete one of the items in the dictionary
stu_dict.popitem()
print(stu_dict)

# Delete one of the dictionaries
stu_dict.pop("age")
print(stu_dict)