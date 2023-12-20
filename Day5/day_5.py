#30 Days Of Python: Day 5
#EXERCISE LEVEL I

# Declare an empty list
empty_list = []

# Declare a list with more than 5 items
five_items = ['Dams', 'Yusuf', 'Jabs', 'Sheba', 'Usman']

# Find the length of your list
print(len(five_items))

# Get the first item, the middle item and the last item of the list
print(five_items[::2])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Salome', '41', '6.5', 'Married', 'Kaduna']

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list using print()
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
print(it_companies[::3])

# Print the list after modifying one of the companies
it_companies[1] = 'Tesla'
print(it_companies)

# Add an IT company to it_companies
it_companies.append('sudo')

# Insert an IT company in the middle of the companies list
it_companies.insert(4, 'Meta')
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[2] = it_companies[2].upper()
print(it_companies)

# Join the it_companies with a string '#;  '
joined_it_companies = '; '.join(it_companies)
print(joined_it_companies)

# Check if a certain company exists in the it_companies list.
comp_exist = 'VR' in it_companies
print(comp_exist)

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
comp_reverse = it_companies.sort(reverse=True)
print(comp_reverse)

# Slice out the first 3 companies from the list
first_three = it_companies[:3]
print(first_three)

# Slice out the last 3 companies from the list
last_three = it_companies[-3:]
print(last_three)

# Slice out the middle IT company or companies from the list
middle_it_comp = it_companies[4:5]
print(middle_it_comp)

# Remove the first IT company from the list
first_pop = it_companies.pop(0)
print(first_pop)

# Remove the middle IT company or companies from the list
del it_companies[3:5]
print(it_companies)

# Remove the last IT company from the list
del it_companies[-1]
print(it_companies)

# Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# Destroy the IT companies list
del it_companies

# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. 
# Then insert Python and SQL after Redux.
full_stack = front_end[:]
full_stack.insert(4, ['Python', 'SQL'])
print(full_stack)

#EXERCISE LEVEL II

# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
list_sort = ages.sort()
print(list_sort)     # min = 19; max = 26

# Add the min age and the max age again to the list
min_max = [19, 26]
add_age = ages.extend(min_max)
print(add_age)

# Find the median age (one middle item or two middle items divided by two)
median_age = ages[4:6]
middle_age = sum(median_age) / 2
print(middle_age)

# Find the average age (sum of all items divided by their number )
average = sum(ages) / len(ages)
print(average)

# Find the range of the ages (max minus min)
range_of_ages = max(min_max) - min(min_max)
print(range_of_ages)

# Compare the value of (min - average) and (max - average), use abs() method
min_diff = abs(min(min_max) - average)
max_diff = abs(max(min_max) - average)
print(min_diff, max_diff)

# Find the middle country(ies) in the countries list
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

middle_country = countries[96:97]
print(middle_country)

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
first_list = countries[:97]
second_list = countries[97:]
print(len(first_list), len(second_list))

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
first, second, third, *scandic = countries
print(f'first is {first}, second is {second}, third is {third} and the scandic countries are {len(scandic)}')
