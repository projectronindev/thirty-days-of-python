# Arithmetic Operations in Python
# Integers

# print('Addition: ', 1 + 2)        # 3
# print('Subtraction: ', 2 - 1)     # 1
# print('Multiplication: ', 2 * 3)  # 6
# print ('Division: ', 4 / 2)       # 2.0  Division in Python gives floating number
# print('Division: ', 6 / 2)        # 3.0         
# print('Division: ', 7 / 2)        # 3.5
# print('Division without the remainder: ', 7 // 2)   # 3,  gives without the floating number or without the remaining
# print ('Division without the remainder: ',7 // 3)   # 2
# print('Modulus: ', 3 % 2)         # 1, Gives the remainder
# print('Exponentiation: ', 2 ** 3) # 8 it means 2 * 2 * 2

# # Floating numbers
# print('Floating Point Number, PI', 3.14)
# print('Floating Point Number, gravity', 9.81)

# Complex numbers
# print('Complex number: ', 1 + 1j)
# print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))

# Declaring the variable at the top first

# a = 3 # a is a variable name and 3 is an integer data type
# b = 2 # b is a variable name and 3 is an integer data type

# # Arithmetic operations and assigning the result to a variable
# total = a + b
# diff = a - b
# product = a * b
# division = a / b
# remainder = a % b
# floor_division = a // b
# exponential = a ** b

# # I should have used sum instead of total but sum is a built-in function - try to avoid overriding built-in functions
# print(total) # if you do not label your print with some string, you never know where the result is coming from
# print('a + b = ', total)
# print('a - b = ', diff)
# print('a * b = ', product)
# print('a / b = ', division)
# print('a % b = ', remainder)
# print('a // b = ', floor_division)
# print('a ** b = ', exponential)

# print('== Addition, Subtraction, Multiplication, Division, Modulus ==')

# # Declaring values and organizing them together
# num_one = 3
# num_two = 4

# # Arithmetic operations
# total = num_one + num_two
# diff = num_two - num_one
# product = num_one * num_two
# div = num_two / num_one
# remainder = num_two % num_one

# # Printing values with label
# print('total: ', total)
# print('difference: ', diff)
# print('product: ', product)
# print('division: ', div)
# print('remainder: ', remainder)

# # Calculating the area of a circle

# radius = input("Enter the radius of a circle: ")
# area_of_circle = 3.14 * float(radius) ** 2
# print("The area of the circle with radius " + radius + " is: ", area_of_circle)

# #Calculating the area of a rectangle

# length = input("Enter the length of a rectangle: ")
# width = input("Enter the width of a rectangle: ")
# area_of_rectangle = float(length) * float(width)
# print("The area of the rectangle with length " + length + " and width " + width + " is: ", area_of_rectangle)

# #Calculating a weigh of an object

# mass = input("Enter the mass of an object in kg: ")
# gravity = 9.81
# weight = float(mass) * gravity
# print("The weight of an object with mass " + mass + " kg is: ", weight, "N")  # N is the unit of weight 

# # Calculating the density of a liquid
# mass = input("Enter the mass of a liquid in kg: ")
# volume = 0.075 # in cubic meter
# density = float(mass) / volume
# print("The density of a liquid with mass " + mass + " kg and volume " + str(volume) + " cubic meter is: ", density, "kg/m^3")  # kg/m^3 is the unit of density

# # Comparison Operators in Python

# print("3 > 2:", 3 > 2)  # True, because 3 is greater than 2
# print("2 > 3:", 2 > 3)  # False, because 2 is not greater than 3
# print("3 >= 2:", 3 >= 2) # True, because 3 is greater than or equal to 2
# print("2 < 3:", 2 < 3)  # True, because 2 is less than 3
# print("3 < 2:", 3 < 2)  # False, because 3 is not less than 2
# print("2 <= 3:", 2 <= 3) # True, because 2 is less than or equal to 3
# print("2 == 3:", 2 == 3) # False, because 2 is not equal to 3
# print("3 == 3:", 3 == 3) # True, because 3 is equal to 3
# print("2 != 3:", 2 != 3) # True, because 2 is not equal to 3

# print("Length of apple:", len("apple"))  # 5
# print("Length of banana:", len("banana"))  # 6
# print("Length of apple == Length of banana:", len("apple") == len("banana"))  # False
# print("Length of apple != Length of banana:", len("apple") != len("banana"))  # True
# print("Length of apple > Length of banana:", len("apple") > len("banana"))  # False
# print("Length of apple < Length of banana:", len("apple") < len("banana"))  # True

# # Comparing something gives either a True or False

# print('True == True: ', True == True)
# print('True == False: ', True == False)
# print('False == False:', False == False)

# # Other Comparison Operators

# print('1 is 1', 1 is 1)                   # True - because the data values are the same
# print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
# print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
# print('B not in Asabeneh', 'B' in 'Asabeneh') # False - there is no uppercase B
# print('coding' in 'coding for all') # True - because coding for all has the word coding
# print('a in an:', 'a' in 'an')      # True
# print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

# #Results as a syntax warning for using is instead of == for comparison

# # Logical Operators in Python

# print("3 > 2 and 4 > 3:", 3 > 2 and 4 > 3) # True - because both statements are true
# print("3 > 2 and 4 < 3:", 3 > 2 and 4 < 3) # False - because the second statement is false
# print("3 < 2 and 4 < 3:", 3 < 2 and 4 < 3) # False - because both statements are false
# print('True and True: ', True and True)
# print("3 > 2 or 4 > 3:", 3 > 2 or 4 > 3)  # True - because both statements are true
# print("3 > 2 or 4 < 3:", 3 > 2 or 4 < 3)  # True - because one of the statements is true
# print("3 < 2 or 4 < 3:", 3 < 2 or 4 < 3)  # False - because both statements are false
# print('True or False:', True or False)
# print("not 3 > 2:", not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
# print("not True:", not True)      # False - Negation, the not operator turns true to false
# print("not False:", not False)     # True
# print("not not True:", not not True)  # True
# print("not not False:", not not False) # False

# EXERCISES

# #3,2,1

# age = 26
# height = 1.75
# complex_num = 1 + 1j

# #4
# Calculate the area of a triangle

# base = input("Enter the base of the triangle: ")
# height = input("Enter the height of the triangle: ")
# area_of_triangle = 0.5 * float(base) * float(height)
# print("The area of the triangle with base " + base + " and height " + height + " is: ", area_of_triangle)

# #5
# Calculate the perimeter of a triangle

# side_a = input("Enter the length of side a of the triangle: ")
# side_b = input("Enter the length of side b of the triangle: ")
# side_c = input("Enter the length of side c of the triangle: ")
# perimeter_of_triangle = float(side_a) + float(side_b) + float(side_c)
# print("The perimeter of the triangle with sides " + side_a + ", " + side_b + ", and " + side_c + " is: ", perimeter_of_triangle)

# #6
# Calculate the area and perimeter of a rectangle

# rectangle_length = input("Enter the length of the rectangle: ")
# rectangle_width = input("Enter the width of the rectangle: ")
# area_of_rectangle = float(rectangle_length) * float(rectangle_width)
# perimeter_of_rectangle = 2 * (float(rectangle_length) + float(rectangle_width))
# print("The area of the rectangle with length " + rectangle_length + " and width " + rectangle_width + " is: ", area_of_rectangle)
# print("The perimeter of the rectangle with length " + rectangle_length + " and width " + rectangle_width + " is: ", perimeter_of_rectangle)

# #7
# Calculate the area and circumference of a circle

# pi = 3.14
# radius = input("Enter the radius of the circle: ")
# area_of_circle = pi * float(radius) * float(radius)
# circumference_of_circle = 2 * pi * float(radius)
# print("The area of the circle with radius " + radius + " is: ", area_of_circle)
# print("The circumference of the circle with radius " + radius + " is: ", circumference_of_circle)

# #8
# # Calculate the slope, x-intercept and y-intercept of y = 2x -2

# m = 2 # slope
# b = -2 # y-intercept
# x_intercept = -b / m # x-intercept
# print("The slope of the line y = 2x - 2 is: ", m)
# print("The y-intercept of the line y = 2x - 2 is: ", b)
# print("The x-intercept of the line y = 2x - 2 is: ", x_intercept)

# #9
# # Calculate the slope and euclidean distance between two points (2, 3) and (10, 8)

# x1, y1 = input("Enter the coordinates of the first point (x1, y1) separated by a comma: ").split(',')
# x2, y2 = input("Enter the coordinates of the second point (x2, y2) separated by a comma: ").split(',')

# x1, y1 = int(x1), int(y1)
# x2, y2 = int(x2), int(y2) 

# slope = (y2 - y1) / (x2 - x1)
# euclidean_distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
# print("The slope between the points (" + str(x1) + ", " + str(y1) + ") and (" + str(x2) + ", " + str(y2) + ") is: ", slope)
# print("The Euclidean distance between the points (" + str(x1) + ", " + str(y1) + ") and (" + str(x2) + ", " + str(y2) + ") is: ", euclidean_distance)

# #10

# print("The maximum value between the slope of the line y = 2x - 2 and the slope between the points is: ", max(m, slope))
# print("The minimum value between the slope of the line y = 2x - 2 and the slope between the points is: ", min(m, slope))

# #12

# len("python")
# len("dragon")

# print(len("python") != len("dragon")) # True - both strings have the same length

# #13
# print('on' in 'python' and 'on' in 'dragon') # True - both strings contain the substring 'on'

# #14
# print('jargon' in 'I hope this course is not full of jargon') # True - the string contains the substring 'jargon'

# #16
# print(not 'on' in 'python' and 'on' in 'dragon')

# #17
# length = len('python')
# len_to_float = float(length)
# float_to_str = str(len_to_float)

# print("The length of the string 'python' is: ", length)
# print("The length of the string 'python' as a float is: ", len_to_float)
# print("The length of the string 'python' as a string is: ", float_to_str)

# #18

# value = 2.7
# int_value = int(value)
# floor_division = 7 // 3
# print("The converted value of 2.7 to an integer is: ", int_value)
# print("The floor division of 7 by 3 is: ", floor_division)
# print("Is the converted integer value equal to the floor division result? ", int_value == floor_division)

# #19

# type_str = type('10')
# type_int = type(10)
# print("Is the type of '10' equal to the type of 10? ", type_str == type_int) # False - because one is a string and the other is an integer

# #20

# print("Is the int value of '9.8' equal to 10? ", int(float('9.8')) == 10) # False - because int(float('9.8')) is 9, not 10

# #21

# hours = input("Enter hours: ")
# rate_per_hour = input("Enter rate per hour: ")
# print("Your weekly earning is: ", float(hours) * float(rate_per_hour))

# #22

# years = input("Enter number of years you have lived: ")
# seconds_in_a_year = 365 * 24 * 60 * 60
# print("You have lived for ", int(years) * seconds_in_a_year, " seconds.")

#23

# Display the table

# for i in range(1, 6):
#     print(i, 1, i, i**2, i**3)