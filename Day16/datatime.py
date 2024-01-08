# Day 16: 30 days of Python programming

from datetime import datetime,date,time,timedelta
# Get the current day, month, year, hour, minute and timestamp from datetime module
now = datetime.now()
print(now) 
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp() #2023-12-11 10:38:24.563048

# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
d = now.strftime("%m/%d/%Y, %H:%M:%S")
print(d) #12/11/2023, 10:38:24


# Today is 5 December, 2019. Change this time string to time.
date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object) #2019-12-05 00:00:00


# Calculate the time difference between now and new year.
t_day = date(2023,12,11)
new_year = date(2024,1,1)
time_to_new_year = new_year - t_day
print(f'Time to new year is {time_to_new_year} ') #Time to new year is 21 days, 0:00:00 


# Calculate the time difference between 1 January 1970 and now.
# Getting the time difference in days
# I have already assigned the current year,month and day from above
print(date(year,month,day) - date(1970,1,1)) #19702 days

# Think, what can you use the datetime module for? Examples:
# -Time series analysis
# -To get a timestamp of any activities in an application
# -Adding posts on a blog