# Day 10 of 30 days of Python

# Iterate 0 to 10 using for loop, do the same using while loop.

# Using for loop to iterate from 0 to 10
for i in range(11):
    print(i)
    i += 1

# Using while loop to iterate from 0 to 10
i = 0
while i <= 10:
    print(i)
    i += 1

# Iterate 10 to 0 using for loop, do the same using while loop.
i = 10
for i in range(10, -1, -1):
    print(i)
    
# Using while loop to iterate from 10 to 0
i = 10
while i >= 0:
    print(i)
    i -= 1

# Write a loop that makes seven calls to print(), so we get on the output the following triangle:

  
  #
  ##
  ###
  ####
  #####
  ######
i = 0
while i <= 7:
    print("#" * i) 
    i += 1

# Use nested loops to create the following:

# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #

for i in range(8):
    row = ''
    for i in range(8):
        row += '# '
    print(row)

# Print the following pattern:

# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100

i = 0
while i <= 10:
    print(f"{i} x {i} = ", i * i )
    i += 1

# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in lst:
    print(i)

# Use for loop to iterate from 0 to 100 and print only even numbers
i = 0
while i <= 100:
    i += 1
    if i % 2 == 0:
        print(i)

# Use for loop to iterate from 0 to 100 and print only odd numbers
i = 0
while i < 100:
    i += 1
    if i % 2 == 1:
        print(i)

# # Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum_of_numbers = 0
for i in range(101):
    sum_of_numbers += i
    i += 1
print("The sum of the numbers is", sum_of_numbers) 

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
sum_of_odd_numbers = 0
sum_of_even_numbers = 0
for i in range(101):
    if i % 2 == 0:
        sum_of_even_numbers += i
    else:
        sum_of_odd_numbers += i
    i += 1
print("Sum of even numbers is ", sum_of_even_numbers)
print("Sum of odd numbers is ", sum_of_odd_numbers)

# This file contains list of countries
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]


land_countries = []
for country in countries:
    if 'land' in country.lower():
        land_countries.append(country)

print("Countries with land: ")
for country in land_countries:
    print(country)

fruit_list = ['banana', 'orange', 'mango', 'lemon']

# Using a for loop to reverse the list
reversed_fruit_list = []
for fruit in reversed(fruit_list):
    reversed_fruit_list.append(fruit)

print("Original fruit list:", fruit_list)
print("Reversed fruit list:", reversed_fruit_list)
