# letter = 'P'                # A string could be a single character or a bunch of texts
# print(letter)               # P
# print(len(letter))          # 1
# greeting = 'Hello, World!'  # String could be made using a single or double quote,"Hello, World!"
# print(greeting)             # Hello, World!
# print(len(greeting))        # 13
# sentence = "I hope you are enjoying 30 days of Python Challenge"
# print(sentence)
# print(len(sentence))

# # Multiline String

# # Triple single quotes
# multiline_string = '''I am a teacher and enjoy teaching.
# I didn't find anything as rewarding as empowering people.
# That is why I created 30 days of python.'''
# print(multiline_string)

# # Triple double quotes
# # Another way of doing the same thing
# multiline_string = """I am a teacher and enjoy teaching.
# I didn't find anything as rewarding as empowering people.
# That is why I created 30 days of python."""
# print(multiline_string)

# # String Concatenation

# first_name = 'Ron Vincent'
# last_name = 'San Juan'
# space = ' '
# full_name = first_name  +  space + last_name
# print(full_name) # Ron Vincent San Juan
# # Checking the length of a string using len() built-in function
# print(len(first_name))  # 11
# print(len(last_name))   # 8
# print(len(first_name) > len(last_name)) # True
# print(len(full_name)) # 20

# # Escape Sequences in Strings

# print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
# print('Days\tTopics\tExercises') # adding tab space or 4 spaces
# print('Day 1\t5\t5')
# print('Day 2\t6\t20')
# print('Day 3\t5\t23')
# print('Day 4\t1\t35')
# print('This is a backslash  symbol (\\)') # To write a backslash
# print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote

# # Old Style String Formatting (%)

# # Strings only
# first_name = 'Ron Vincent'
# last_name = 'San Juan'
# language = 'Python'
# formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
# print(formated_string)

# # Strings  and numbers
# radius = 10
# pi = 3.14
# area = pi * radius ** 2
# formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area) # 2 refers the 2 significant digits after the point
# print(formated_string) # The area of circle with a radius 10 is 314.00.

# python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
# formated_string = 'The following are python libraries:%s' % (python_libraries)
# print(formated_string) # "The following are python libraries:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"

# # New Style String Formatting (str.format())

# first_name = 'Ron Vincent'
# last_name = 'San Juan'
# language = 'Python'
# formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
# print(formated_string)
# a = 4
# b = 3

# print('{} + {} = {}'.format(a, b, a + b))
# print('{} - {} = {}'.format(a, b, a - b))
# print('{} * {} = {}'.format(a, b, a * b))
# print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
# print('{} % {} = {}'.format(a, b, a % b))
# print('{} // {} = {}'.format(a, b, a // b))
# print('{} ** {} = {}'.format(a, b, a ** b))


# # Strings  and numbers
# radius = 10
# pi = 3.14
# area = pi * radius ** 2
# formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
# print(formated_string)

# # String Interpolation

# a = 4
# b = 3
# print(f'{a} + {b} = {a +b}')
# print(f'{a} - {b} = {a - b}')
# print(f'{a} * {b} = {a * b}')
# print(f'{a} / {b} = {a / b:.2f}')
# print(f'{a} % {b} = {a % b}')
# print(f'{a} // {b} = {a // b}')
# print(f'{a} ** {b} = {a ** b}')

# # Unpacking a Sequence into Variables

# language = 'Python'
# a,b,c,d,e,f = language # unpacking sequence characters into variables
# print(a) # P
# print(b) # y
# print(c) # t
# print(d) # h
# print(e) # o
# print(f) # n

# # Accessing Characters in Strings by Index

# language = 'English'
# first_letter = language[0] # E
# second_letter = language[1] # n
# last_index = len(language) - 1
# last_letter = language[last_index] # h
# print("First letter in", language, "is: ", first_letter)
# print("Second letter in", language, "is: ", second_letter)
# print("Last letter in", language, "is: ", last_letter)

# # Use negative to start from the end of the string
# last_letter_negative = language[-1] # h
# print("Last letter in", language, "is: ", last_letter_negative)

# # Slicing strings

# language = 'Python'
# first_three = language[0:3] # starts at zero index and up to 3 but not include 3
# print(first_three) #Pyt
# last_three = language[3:6]
# print(last_three) # hon
# # Another way
# last_three = language[-3:]
# print(last_three)   # hon
# last_three = language[3:]
# print(last_three)   # hon

# # Reversing a string

# greeting = 'Hello, World!'
# print(greeting[::-1]) # !dlroW ,olleH

# # Skipping Characters While Slicing

# language = 'Python'
# pto = language[0:6:2] #
# print(pto) # Pto

# # String Methods

# # capitalize()
# word = 'python'
# print(f"Without using capitalize: {word}") # python
# print(f"With capitalize: {word.capitalize()}") # Python

# # count()

# sentence = 'I am enjoying 30 days of python'
# print(f"Without using count: {sentence}") # I am enjoying 30 days
# print(f"Count of 'o' in \"{sentence}\": {sentence.count('o')}") # 3
# print(f"Characters 10 to 20 in \"{sentence}\": {sentence[10:20]}")
# print(f"Count of 'y' in \"{sentence}\": {sentence.count('y', 10, 20)}") # 1

# # endswith()

# sentence = 'I am enjoying 30 days of python'
# print(f"Without using endswith: {sentence}") # I am enjoying 30 days of python
# print(f"Does \"{sentence}\" ends with 'on'? : {sentence.endswith('on')}") # True
# print(f"Does \"{sentence}\" ends with 'tion'? : {sentence.endswith('tion')}") # False

# # expandtabs()

# sentence = 'I\tam\tenjoying\t30\tdays\tof\tpython'
# print(f"Without using expandtabs: {sentence}") # I	am	enjoying	30	days	of	python
# print(f"With expandtabs: {sentence.expandtabs()}") # I       am      enjoying 30      days    of      python
# print(f"With expandtabs(10): {sentence.expandtabs(10)}") # I         am        enjoying 30        days      of        python

# # find()

# sentence = 'I am enjoying 30 days of python'
# print(f"Without using find: {sentence}") # I am enjoying 30 days of python
# print(f"Index of 'y' in \"{sentence}\": {sentence.find('y')}") # 9
# print(f"Index of 'th' in \"{sentence}\": {sentence.find('th')}") # 27
# print(f"Index of 'r' in \"{sentence}\": {sentence.find('r')}") # -1

# # rfind()

# sentence = 'I am enjoying 30 days of python'
# print(f"Without using rfind: {sentence}") # I am enjoying 30 days of python
# print(f"Index of 'y' in \"{sentence}\": {sentence.rfind('y')}") # 26
# print(f"Index of 'n' in \"{sentence}\": {sentence.rfind('n')}") # 30
# print(f"Index of 'r' in \"{sentence}\": {sentence.rfind('r')}") # -1

# # format()

# first_name = 'Ron Vincent'
# last_name = 'San Juan'
# age = 26
# prog_language = 'Python'
# sentence = 'Hi, I am {} {}. I am {} years old. Currently learning {}.'.format(first_name, last_name, age, prog_language)
# print(sentence)

# radius = 10
# pi = 3.14
# area = pi * radius ** 2
# result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
# print(result) # The area of a circle with radius 10 is 314

# # index()

# sentence = 'I am enjoying 30 days of python'
# sub_string = '30'
# print(f"Without using index: {sentence}") # I am enjoying 30 days of python
# print(f"Index of '{sub_string}' in \"{sentence}\": {sentence.index(sub_string)}") # 13
# print(sentence.index(sub_string, 10)) # 13

# # rindex()

# sentence = 'I am enjoying 30 days of python'
# sub_string = 'da'
# print(f"Without using rindex: {sentence}") # I am enjoying 30 days of python
# print(f"rindex of '{sub_string}' in \"{sentence}\": {sentence.rindex(sub_string)}") # 17
# print(sentence.rindex(sub_string, 10)) # 17

# # alnum()

# sentence_withspace = "I am enjoying 30 days of python" # False, space is excluded
# sentence_withoutspace = "Iamenjoying30daysofpython" # True
# print(f"Without using isalnum: {sentence_withspace}") # I am enjoying 30 days
# print(sentence_withspace.isalnum())

# # isalpha()

# sentence_withspace = "thirty days of python" # False, space is excluded
# sentence_withoutspace = "thirtydaysofpython"
# print(f"Without using isalpha: {sentence_withoutspace}")
# print(sentence_withoutspace.isalpha())

# # isdecimal()

# challenge = 'thirty days of python'
# print(challenge.isdecimal())  # False
# challenge = '123'
# print(challenge.isdecimal())  # True
# challenge = '\u00B2'
# print(challenge.isdigit())   # True 
# challenge = '12 3'
# print(challenge.isdecimal())  # False, space not allowed

# # isdigit()

# challenge = 'Thirty'
# print(challenge.isdigit()) # False
# challenge = '30'
# print(challenge.isdigit())   # True
# challenge = '\u00B2'
# print(challenge.isdigit())   # True

# # isnumberic()

# num = '10'
# print(num.isnumeric()) # True
# num = '\u00BD' # ½
# print(num.isnumeric()) # True
# num = '10.5'
# print(num.isnumeric()) # False

# # isidentifier()

# challenge = '30DaysOfPython'
# print(challenge.isidentifier()) # False, because it starts with a number
# challenge = 'thirty_days_of_python'
# print(challenge.isidentifier()) # True

# # islower()

# challenge = 'thirty days of python'
# print(challenge.islower()) # True
# challenge = 'Thirty days of python'
# print(challenge.islower()) # False

# # isupper()

# challenge = 'thirty days of python'
# print(challenge.isupper()) #  False
# challenge = 'THIRTY DAYS OF PYTHON'
# print(challenge.isupper()) # True

# # join()

# web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
# result = ' '.join(web_tech)
# print(result) # 'HTML CSS JavaScript React'

# # strip()
# challenge = 'thirty days of pythoonnn'
# print(challenge.strip('thon')) # 'irty days of py'

# # replace()
# challenge = 'thirty days of python'
# print(challenge.replace('python', 'coding')) # 'thirty days of coding'

# # split()
# challenge = 'thirty days of python'
# print(challenge.split()) # ['thirty', 'days', 'of', 'python']
# challenge = 'thirty, days, of, python'
# print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']

# # title()
# challenge = 'thirty days of python'
# print(challenge.title()) # Thirty Days Of Python

# # swapcase()
# challenge = 'thirty days of python'
# print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
# challenge = 'Thirty Days Of Python'
# print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

# # startswith()
# challenge = 'thirty days of python'
# print(challenge.startswith('thirty')) # True

# challenge = '30 days of python'
# print(challenge.startswith('thirty')) # False

# EXERCISES

# 1
# sentence = 'Thirty' + ' ' + 'Days'  + ' ' + 'Of'  + ' ' + 'Python'
# print(sentence)

# 2
# sentence = 'Coding' + ' ' + 'For'  + ' ' + 'All'
# print(sentence)

# 3
# company = "Coding For All"
# print(company)

# 4
# company = "Coding For All"
# print(company)

# 5
# company = "Coding For All"
# print(len(company))

# 6
# company = "Coding For All"
# print(company.upper())

# 7
# company = "Coding For All"
# print(company.lower())

# 8
# company = "coding for all"
# print(company.capitalize())
# print(company.title())
# print(company.swapcase())

# 9
# company = "coding for all"
# print(company.strip('coding'))

# 10
# company = "Coding For All"
# print(company.index('Coding'))
# print(company.find('Coding'))

# 11
# company = "Coding For All"
# print(company.replace('Coding', 'Gaming'))

# 12
# company = "Python for Everyone"
# print(company)
# print(company.replace('Everyone', 'All'))

# 13
# company = "Coding For All"
# print(company.split(' '))

# 14
# sentence = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
# print(sentence)
# print(sentence.split(', '))

# 15
# company = "Coding For All"
# print(company[0])

# 16
# company = "Coding For All"
# print(company.rindex('l'))

# 17
# company = "Coding For All"
# print(company[10])

# 18
# abb_python = "Python For Everyone"
# print(abb_python[abb_python.find('P')] + abb_python[abb_python.find('F')] + abb_python[abb_python.find('E')])

# 19
# abb_coding = "Coding For All" 
# print(abb_coding[abb_coding.find('C')] + abb_coding[abb_coding.find('F')] + abb_coding[abb_coding.find('A')])

# 20
# company = "Coding For All"
# print(company.index('C'))

# 21
# company = "Coding For All"
# print(company.index('F'))

# 22
# company = "Coding For All People"
# print(company.rfind('l'))

# 23
# sentence = "You cannot end a sentence with because because because is a conjunction"
# print(sentence.find('because'))

# 24
# sentence = "You cannot end a sentence with because because because is a conjunction"
# print(sentence.rfind('because'))

# 25
# sentence = 'You cannot end a sentence with because because because is a conjunction'
# print(sentence.replace('because', ''))

# 26
# sentence = 'You cannot end a sentence with because because because is a conjunction'
# print(sentence.find('because'))

# 27
# sentence = 'You cannot end a sentence with because because because is a conjunction'
# print(sentence[sentence.find('because'):sentence.rfind('because')])

# 28 29
# company = "Coding For All"
# print(company.startswith('Coding'))
# print(company.endswith('coding'))

# 30
# company = '   Coding For All      '
# company.strip()

#31
# variable1 = '30DaysOfPython'
# variable2 = 'thirty_days_of_python'
# print(variable1.isidentifier())
# print(variable2.isidentifier())

#32
# py_lib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
# sentence = ' '.join(py_lib)
# print(sentence)

# 33
# sentences = '''I am enjoying this challenge.\n
# I just wonder what is next.'''
# print(sentences)

# 34
# print("Name\tAge\tCountry\t City")
# print("Ron\t25\tPhilippines\t Makati")

# 35
# radius = 10
# area = 3.14 * radius ** 2
# print("The area of a circle with radius %s is %s meters square."%(radius, area))

# 36

# a = 8
# b = 6

# print('{} + {} = {}'.format(a, b, a + b))
# print('{} - {} = {}'.format(a, b, a - b))
# print('{} * {} = {}'.format(a, b, a * b))
# print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
# print('{} % {} = {}'.format(a, b, a % b))
# print('{} // {} = {}'.format(a, b, a // b))
# print('{} ** {} = {}'.format(a, b, a ** b))