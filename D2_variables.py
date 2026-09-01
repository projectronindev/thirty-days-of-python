# Variables in Python

# first_name = 'Ron Vincent'
# last_name = 'San Juan'
# country = 'Philippines'
# city = 'Manila'
# age = 26
# is_married = False
# skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
# person_info = {
#    'firstname':'Ron Vincent',
#    'lastname':'San Juan',
#    'country':'Philippines',
#    'city':'Manila'
#    }

# Printing the values stored in the variables

# print('First name:', first_name)
# print('First name length:', len(first_name))
# print('Last name: ', last_name)
# print('Last name length: ', len(last_name))
# print('Country: ', country)
# print('City: ', city)
# print('Age: ', age)
# print('Married: ', is_married)
# print('Skills: ', skills)
# print('Person information: ', person_info)

#Declaring Multiple Variables in One Line

# first_name, last_name, country, age, is_married = 'Ron Vincent', 'San Juan', 'Philippines', 26, False

# print(first_name, last_name, country, age, is_married)
# print('First name:', first_name)
# print('Last name: ', last_name)
# print('Country: ', country)
# print('Age: ', age)
# print('Married: ', is_married)

# Getting user input using input() function
# first_name = input('What is your first name? ')
# age = input('How old are you? ')

# print('First name:', first_name)
# print('Age:', age)

# Checking data types of variables

# print(type(first_name))
# print(type(last_name))
# print(type(country))
# print(type(age))
# print(type(is_married))
# print(type(skills))
# print(type(person_info))

# Casting (converting) data types in Python

#Convert int to float

# num_int = 5 #Declared an integer value
# print('Int:', num_int, type(num_int))

# num_float = float(num_int) #Converted int to float
# print('Float:', num_float, type(num_float))

#Convert float to int

# num_float = 5.0 #Declared a float value
# print('Float:', num_float, type(num_float))

# num_int = int(num_float) #Converted float to int
# print('Int:', num_int, type(num_int))

#Convert int to str
# num_int = 10 #Declared an integer value
# print('Int:', num_int, type(num_int))

# num_str = str(num_int) #Converted int to str
# print('Str:', num_str, type(num_str))

#Convert str to int or float
# num_str = '10' #Declared a string value
# num_float = float(num_str) #Converted str to float
# num_int = int(num_str) #Converted str to int
# print('Str:', num_str, type(num_str))
# print('Float:', num_float, type(num_float))
# print('Int:', num_int, type(num_int))

#Convert str to list
# str = 'Python' #Declared a string value
# print('Str:', str, type(str))
# list_str = list(str) #Converted str to list
# print('List:', list_str, type(list_str))

#EXERCISES

# Day 2

# first_name = 'Ron Vincent'
# last_name = 'San Juan'
# full_name = first_name + ' ' + last_name
# country = 'Philippines'
# city = 'Manila'
# age = 26
# year = 2026
# is_married = False
# is_true = True
# is_light_on = False
# work, school, home = 'Work', 'School', 'Home'

# print('First name:', first_name, type(first_name))
# print('Last name:', last_name, type(last_name))
# print('Full name:', full_name, type(full_name))
# print('Country:', country, type(country))
# print('City:', city, type(city))
# print('Age:', age, type(age))
# print('Year:', year, type(year))
# print('Married:', is_married, type(is_married))
# print('Is true:', is_true, type(is_true))
# print('Is light on:', is_light_on, type(is_light_on))
# print('Work:', work, type(work))
# print('School:', school, type(school))
# print('Home:', home, type(home))

# length_first_name = len(first_name)
# length_last_name = len(last_name)
# print('Length of first name:', length_first_name, type(length_first_name))
# print('Length of last name:', length_last_name, type(length_last_name))

# num_one = 5
# num_two = 4

# total = num_one + num_two
# diff = num_one - num_two
# product = num_one * num_two
# division = num_one / num_two
# remainder = num_one % num_two
# exponent = num_one ** num_two
# floor_division = num_one // num_two

# print('Total:', total, type(total))
# print('Difference:', diff, type(diff))
# print('Product:', product, type(product))
# print('Division:', division, type(division))
# print('Remainder:', remainder, type(remainder))
# print('Exponent:', exponent, type(exponent))
# print('Floor Division:', floor_division, type(floor_division))

# # Radius of a circle
# radius = 30 # radius of a circle
# area_of_circle = 3.14 * radius ** 2 # area of a circle
# circum_of_circle = 2 * 3.14 * radius # circumference of a circle

# print('Area of circle:', area_of_circle)
# print('Circumference of circle:', circum_of_circle)

# input_radius = input('Enter radius: ')
# area_of_circle = 3.14 * int(input_radius) ** 2 # area of a circle
# circum_of_circle = 2 * 3.14 * int(input_radius) # circumference

# print('Area of circle:', area_of_circle)
# print('Circumference of circle:', circum_of_circle)

# input_first_name = input('What is your first name? ')
# input_last_name = input('What is your last name? ')
# input_country = input('What country are you from? ')
# input_age = input('How old are you? ')

# print('First name:', input_first_name)
# print('Last name:', input_last_name)
# print('Country:', input_country)
# print('Age:', input_age)