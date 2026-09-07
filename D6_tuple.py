# # Creating a Tuple

# empty_tuple = tuple()
# empty_tuple = ()

# tpl = ('item1', 'item2', 'item3', 'item4', 'item5')
# print(tpl) # ('item1', 'item2', 'item3', 'item4', 'item5')

# fruits = ('banana', 'orange', 'mango', 'lemon')
# print(fruits) # ('banana', 'orange', 'mango', 'lemon')

# # Tuple Length
# print(len(tpl)) # 5
# print(len(fruits)) # 4

# Accessing Tuple Items

# # Positive Indexing

# countries = ('Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway')
# print(countries) # ('Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway')

# first_country = countries[0]
# print('First country:', first_country) # Finland

# last_country = countries[4]
# print('Last country:', last_country) # Norway

# # Negative Indexing

# fruits = ('banana', 'orange', 'mango', 'lemon')
# print(fruits) # ('banana', 'orange', 'mango', 'lemon')

# first_fruit = fruits[-4]
# print('First fruit:', first_fruit) # banana

# last_fruit = fruits[-1]
# print('Last fruit:', last_fruit) # lemon

# # Slicing Tuples

# # Positive Indexing

# tpl = ('banana', 'orange', 'mango', 'lemon', 'lime', 'apple')
# get_all_fruits = tpl[0:6] # we are slicing all the items from index 0 to index 6
# print(get_all_fruits)

# # No end index

# get_some_fruits = tpl[1:4] # get the fruits starting from index 1 to 3
# print(get_some_fruits) # ('orange', 'mango', 'lemon')

# # No step

# get_every_other_fruit = tpl[::2] # get every second fruit
# print(get_every_other_fruit) # ('banana', 'mango', 'lime')

# # Negative Indexing

# fruits = ('banana', 'orange', 'mango', 'lemon', 'lime', 'apple')
# all_fruits = fruits[-6:] # we are slicing all the items from index -6 to index -1
# print(all_fruits) # ('banana', 'orange', 'mango', 'lemon', 'lime', 'apple')

# # No end index
# get_some_fruits = fruits[-3:] # get the fruits starting from index -3
# print(get_some_fruits) # ('lemon', 'lime', 'apple')

# # No step
# get_every_other_fruit = fruits[::-2] # get every second fruit in reverse order
# print(get_every_other_fruit) # ('apple', 'lemon', 'orange')

# # Changing Tuples to Lists
# countries = ('Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway')
# print('Tuple:', countries) # ('Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway')

# countries = list(countries) # changing tuple to list
# print('List:', countries) # ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# countries[0] = 'New Zealand' # changing the first item
# print('Changed List:', countries) # ['New Zealand', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# countries = tuple(countries) # changing list back to tuple
# print('Changed Tuple:', countries) # ('New Zealand', 'Estonia', 'Denmark', 'Sweden', 'Norway')


# # Check if item is in the tuple

# fruits = ('banana', 'orange', 'mango', 'lemon')
# does_exist = 'banana' in fruits # check if banana is in the list
# print(does_exist) # True

# # Joining Tuples

# # Using plus operator

# tpl_items1 = ('item1', 'item2', 'item3')
# tpl_items2 = ('item4', 'item5', 'item6')
# combined_tpl = tpl_items1 + tpl_items2

# print(combined_tpl) # ('item1', 'item2', 'item3', 'item4', 'item5', 'item6')

# # Deleting Tuples

# sample_tpl = ('item1', 'item2', 'item3', 'item4', 'item5')
# del sample_tpl # deleting the tuple
# # print(sample_tpl) # NameError: name 'sample_tpl' is not defined