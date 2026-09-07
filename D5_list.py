# var_list = list()
# empty_list = list()
# print(len(var_list)) # 0

# square_bracket_list = []
# print(len(square_bracket_list)) # 0

# fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
# vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
# animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
# web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
# countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway'] # list of countries

# # Print the lists and its length
# print('Fruits:', fruits)
# print('Number of fruits:', len(fruits))
# print('Vegetables:', vegetables)
# print('Number of vegetables:', len(vegetables))
# print('Animal products:',animal_products)
# print('Number of animal products:', len(animal_products))
# print('Web technologies:', web_techs)
# print('Number of web technologies:', len(web_techs))
# print('Countries:', countries)
# print('Number of countries:', len(countries))

# diff_type_list = ['Ron', 26, 5.2, True, 'San Juan'] # list containing different data types
# print('List with different data types:', diff_type_list)

# Accessing List Items Using Positive Indexing

# fruits = ['banana', 'orange', 'mango', 'lemon']
# print('Fruits:', fruits)
# first_fruit = fruits[0] # we are accessing the first item using its index
# print('First fruit:', first_fruit) # banana
# last_fruit = fruits[3] # we are accessing the last item using its index
# print('Last fruit:', last_fruit) # lemon

# Accessing List Items Using Negative Indexing

# countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']
# print('Countries:', countries)
# first_country = countries[-5] # we are accessing the first item using its negative index
# print('First country:', first_country) # Finland
# last_country = countries[-1] # we are accessing the last item using its negative index
# print('Last country:', last_country) # Norway

# # Unpacking List Items

# list_items = ['item1', 'item2', 'item3', 'item4', 'item5']
# first_item, second_item, third_item, *the_rest = list_items
# print('First item:', first_item) # item1
# print('Second item:', second_item) # item2
# print('Third item:', third_item) # item3
# print('The rest of the items:', the_rest) # ['item4', 'item5]

# # First Example
# fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
# first_fruit, second_fruit, third_fruit, *rest = fruits 
# print(first_fruit)     # banana
# print(second_fruit)    # orange
# print(third_fruit)     # mango
# print(rest)           # ['lemon','lime','apple']

# # Second Example about unpacking list
# first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
# print(first)          # 1
# print(second)         # 2
# print(third)          # 3
# print(rest)           # [4,5,6,7,8,9]
# print(tenth)          # 10

# # Third Example about unpacking list
# countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
# gr, fr, bg, sw, *scandic, es = countries
# print(gr) 
# print(fr)
# print(bg)
# print(sw)
# print(scandic)
# print(es)

# # Slicing Items from a List

# #Positive Indexing

# lst = ['banana', 'orange', 'mango', 'lemon', 'lime', 'apple']
# get_all_fruits = lst[0:6] # we are slicing all the items from index 0 to index 6
# print(get_all_fruits)

# # No end index

# get_some_fruits = lst[1:] # get the fruits starting from index 1
# print(get_some_fruits) # ['orange', 'mango', 'lemon', 'lime', 'apple']

# # No step

# get_every_other_fruit = lst[::2] # get every second fruit
# print(get_every_other_fruit) # ['banana', 'mango', 'lime']

# # Negative Indexing

# fruits = ['banana', 'orange', 'mango', 'lemon', 'lime', 'apple']
# all_fruits = fruits[-6:] # we are slicing all the items from index -6 to index -1
# print(all_fruits) # ['banana', 'orange', 'mango', 'lemon', 'lime', 'apple']

# # No end index

# get_some_fruits = fruits[-3:] # get the fruits starting from index -3
# print(get_some_fruits) # ['lemon', 'lime', 'apple']

# # No step
# get_every_other_fruit = fruits[::-2] # get every second fruit in reverse order
# print(get_every_other_fruit) # ['apple', 'lemon', 'orange']

# # Check if item is in the list

# fruits = ['banana', 'orange', 'mango', 'lemon']
# does_exist = 'banana' in fruits # check if banana is in the list
# print(does_exist) # True

# # Adding items in a list

# fruits = []
# fruits.append('banana') # add banana in the list
# print(fruits) # ['banana']

# country = list()
# country.append('Philippines') # add Philippines in the list
# print(country) # ['Philippines']

# # Inserting items in a list

# asian_countries = ['Philippines', 'China', 'Japan', 'Korea']
# asian_countries.insert(2, 'South Korea') # insert South Korea at index 2
# print(asian_countries) # ['Philippines', 'China', 'South Korea', 'Japan', 'Korea']
# asian_countries.insert(0, 'Singapore') # insert Singapore at index 0
# print(asian_countries) # ['Singapore', 'Philippines', 'China', 'South Korea', 'Japan', 'Korea']

# # Removing items from a list

# subjects = ['Math', 'English', 'Science', 'History', 'Geography']
# subjects.remove('History') # remove History from the list
# print(subjects) # ['Math', 'English', 'Science', 'Geography']

# # Removing Items Using pop()

# vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
# print(vegetables) # ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']

# vegetables.pop() # remove the last item from the list
# print(vegetables) # ['Tomato', 'Potato', 'Cabbage','Onion']

# vegetables.pop(3) # remove the fourth item from the list
# print(vegetables) # ['Tomato', 'Potato', 'Cabbage']

# # Removing Items Using del

# sample_list = ['item1', 'item2', 'item3']
# print(sample_list) # ['item1', 'item2', 'item3']

# del sample_list[0] # remove the first item from the list
# print(sample_list) # ['item2', 'item3']

# del sample_list[1:2] # remove items starting from index 1 to index 2
# print(sample_list) # ['item2']

# del sample_list # delete the entire list
# print(sample_list) # NameError: name 'sample_list' is not defined

# # Clearing List Items

# sample_list = ['item1', 'item2', 'item3']
# print(sample_list) # ['item1', 'item2', 'item3']

# sample_list.clear() # clear the list items
# print(sample_list) # []

# # Copying a List

# original_list = ['item1', 'item2', 'item3']
# copied_list = original_list.copy()
# print('Original List:', original_list) # ['item1', 'item2', 'item3']
# print('Copied List:', copied_list) # ['item1', 'item2', 'item3']

# # Joining Lists

# # Using plus operator

# positive_numbers = [1, 2, 3]
# zero = [0]
# negative_numbers = [-3, -2, -1]
# numbers = positive_numbers + zero + negative_numbers

# print('Positive Numbers:', positive_numbers) # [1, 2, 3]
# print('Zero:', zero) # [0]
# print('Negative Numbers:', negative_numbers) # [-3, -2, -1]
# print('Joined List:', numbers) # [1, 2, 3, 0, -3, -2, -1]

# # Using extend() method

# list_1 = ['item1', 'item2', 'item3']
# list_2 = ['item4', 'item5', 'item6']
# list_1.extend(list_2) # join list_2 to list_1
# print('Extended List:', list_1) # ['item1', 'item2', 'item3', 'item4', 'item5', 'item6']

# positive_numbers = [1, 2, 3]
# zero = [0]
# negative_numbers = [-3, -2, -1]

# negative_numbers.extend(zero) # join zero to negative_numbers
# negative_numbers.extend(positive_numbers) # join positive_numbers to negative_numbers

# print('Positive Numbers:', positive_numbers) # [1, 2, 3]
# print('Zero:', zero) # [0]
# print('Negative Numbers:', negative_numbers) # [-3, -2, -1, 0, 1, 2, 3]

# # Counting List Items

# sample_list = ['item1', 'item2', 'item3', 'item1', 'item1']
# print('Sample List:', sample_list) # ['item1', 'item2', 'item3', 'item1', 'item1']
# print('Count of item1:', sample_list.count('item1')) # 3

# # Finding index of an Item in a List

# sample_list = ['item1', 'item2', 'item3', 'item1', 'item2']
# print('Sample List:', sample_list) # ['item1', 'item2', 'item3']
# print('Index of item1:', sample_list.index('item1')) # 0
# print('Index of item2:', sample_list.index('item2')) # 1 checking the first occurrence of item2

# # Reversing a list

# right_order = ['item1', 'item2', 'item3']
# print('Right Order:', right_order) # ['item1', 'item2', 'item3']

# right_order.reverse() # reverse the list
# print('Reversed Order:', right_order) # ['item3', 'item2', 'item1']

# # Sorting List Items

# sample_list = ['item3', 'item1', 'item2']
# print('Sample List:', sample_list) # ['item3', 'item1', 'item2']

# sample_list.sort() # ascending order
# print('Sorted List (Ascending Order):', sample_list) # ['item1', 'item2', 'item3']

# sample_list.sort(reverse=True) # descending order
# print('Sorted List (Descending Order):', sample_list) # ['item3', 'item2', 'item1'] 
